from pathlib import Path
'''
data=Path("datasets/raw_data/member_list.py")
if data.exists():
    print(f"Found the dataset at: {data}")
else:
    data.parent.mkdir(parents=True, exist_ok=True)
    data.touch()

for item in data.parent.iterdir():
    if item.suffix==".py":
        print(f"Found a dataset: {item.name}")
    else:
        print(f"Not a dataset: {item.name}")
'''
from pathlib import Path

# 1. Setup the path
data_dir = Path("datasets/raw_data")
data_dir.mkdir(parents=True, exist_ok=True)

# 2. Touch a file to ensure the folder isn't empty for our test
(data_dir / "member_list.py").touch()

# 3. RECURSIVE Search using rglob
# rglob("*.py") means "Search this folder and ALL subfolders for .py files"
print("--- Recursive Python File Search ---")
py_files = list(data_dir.rglob("*.py"))

if not py_files:
    print("No Python files found.")
else:
    for file in py_files:
        print(f"Found: {file.name} at {file.parent}")