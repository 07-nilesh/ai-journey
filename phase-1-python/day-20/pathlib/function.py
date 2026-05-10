from pathlib import Path

# 1. cwd() - Finding our current "Office"
current_work_dir = Path.cwd()
print(f"📍 Script is running from: {current_work_dir}")

# 2. home() - Locating the "Boss's Cabin" (Global user settings)
user_home = Path.home()
print(f"🏠 User's home directory: {user_home}")

# 3. / operator - Designing the "Digital Locker" structure
# This joins: current_dir / SPOTTER_PROJECT / datasets / raw_data
data_folder = current_work_dir / "SPOTTER_PROJECT" / "datasets" / "raw_data"

# 4. exists() and mkdir() - Building the office if it's not there
if not data_folder.exists():
    print("🚧 Dataset folder missing. Creating now...")
    # parents=True creates the whole chain (SPOTTER_PROJECT, datasets, etc.)
    data_folder.mkdir(parents=True, exist_ok=True)
    
    # Let's create a dummy file to test with
    (data_folder / "member_list.csv").touch()
    (data_folder / "bicep_curl.jpg").touch()

print(f"✅ Data folder verified at: {data_folder}")

# 5. iterdir(), name, suffix, parent - The "Inventory Taker"
print("\n--- Scanning Data Locker ---")
for item in data_folder.iterdir():
    # .name gives the full filename
    # .suffix gives the extension (like .csv or .jpg)
    # .parent gives the folder object it sits in
    print(f"File Found: {item.name}")
    print(f"  - Extension: {item.suffix}")
    print(f"  - Location: {item.parent.name}")
    
    if item.suffix == ".csv":
        print(f"  👉 Found a Dataset: {item.name}")