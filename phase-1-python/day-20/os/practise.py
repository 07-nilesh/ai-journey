import os
pid=os.getpid()
print(f"Current process ID: {pid}")

current_dir=os.getcwd()
print(f"Current working directory: {current_dir}")

path_env=os.getenv("PYTHONPATH","Not Set")
print(f"System PYTHONPATH variable: {path_env}")

folder_path="datasets"
path=os.path.join(current_dir, folder_path,"experiments","trial_1")
print(f"Constructed path: {path}")
if os.path.exists(path):
    print("Path exists, ready to save data.")
else:
    print("Path does not exist, creating directories...")
    os.makedirs(path)
    print(f"Directories created at: {path}")
