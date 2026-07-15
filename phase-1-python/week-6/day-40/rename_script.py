from pathlib import Path

def rename_script(target_dir,pattern_prefix):
    target_path=Path(target_dir)

    match_files=list(target_path.glob("*.csv"))
    for index,file_path in enumerate(match_files,start=1):
        try:
            new_name=f"{pattern_prefix.strip()}_{index:02d}{file_path.suffix}"
            new_file_path=file_path.with_name(new_name)

            file_path.rename(new_file_path)
            print(f"Renamed:{file_path.name}->{new_name}")
        except FileNotFoundError:
            print(f"Error: Target file vanished during execution: {file_path}")
        except PermissionError:
            print(f"Error: Insufficient OS privileges to rename: {file_path}")