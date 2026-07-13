from pathlib import Path

target=Path("campus_logs")
if target.exists():
    for i in target.iterdir():
        if i.is_file() and i.suffix==".logs":
            print(f"discovered : {i.stem}")
else:
    print("target path does not exists")