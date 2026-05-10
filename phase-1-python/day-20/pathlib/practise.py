from pathlib import Path

current_work_dir = Path.cwd()
backup = current_work_dir / "backup"

# Pro move: This one line replaces your entire if/else block!
# parents=True: creates all missing folders in the path
# exist_ok=True: doesn't crash if the folder is already there
backup.mkdir(parents=True, exist_ok=True)
(backup / "model_weights.h5").touch()  # Simulate creating a file in the backup folder
print(f"✅ Backup folder ready at: {backup}")

# Listing files
for item in backup.iterdir():
    # Pro Tip: .suffix returns things like '.py' or '.csv'
    print(f"File: {item.name} | Type: {item.suffix} | Parent: {item.parent.name}")