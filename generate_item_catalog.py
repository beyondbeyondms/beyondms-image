import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOTS = [
    ("Character", True),  # (folder name, has category subfolders)
    ("Mob", False),
    ("Item", True),
]

entries = []

for root_name, has_categories in ROOTS:
    root_path = BASE_DIR / root_name
    if not root_path.exists():
        continue

    if has_categories:
        for category_dir in sorted(p for p in root_path.iterdir() if p.is_dir()):
            category = category_dir.name
            for file_path in sorted(category_dir.glob("*.png")):
                item_id = file_path.stem
                entries.append({
                    "itemId": item_id,
                    "character": root_name,
                    "category": category,
                })
    else:
        for file_path in sorted(root_path.glob("*.png")):
            item_id = file_path.stem
            entries.append({
                "itemId": item_id,
                "character": root_name,
                "category": root_name,
            })

output_path = BASE_DIR / "items.json"
with output_path.open("w", encoding="utf-8") as f:
    json.dump(entries, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Wrote {len(entries)} entries to {output_path}")
