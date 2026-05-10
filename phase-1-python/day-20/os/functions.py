import os

#1 os.path.join() is like the AI's GPS for file paths. It helps us create correct paths regardless of the operating system we're on (Windows, macOS, Linux).
folder = "datasets"
subfolder = "gym_images"
filename = "bench_press.jpg"

# The WRONG way: path = folder + "/" + filename (Will break on Windows)
# The AI Engineer way:
path = os.path.join(folder, subfolder, filename)
print(f"Path for our AI to find: {path}")

#2 os.listdir() is like the AI's way of checking what's in a folder. It lists all files and subfolders inside a given directory.
print("\nContents of the 'datasets' folder:")
try:
    contents = os.listdir(folder)
    for item in contents:
        print(f"- {item}")
except FileNotFoundError:
    print("Folder not found.")
except PermissionError:
    print("Permission denied to access the folder.")

#3 os.path.exists() and os.makedirs() are the AI's way of double-checking if a file or folder is actually there before trying to use it. It returns True if the path exists, and False if it doesn't.
print("\nChecking if our image file exists:")   
output_dir = "spotter_model_weights"

if not os.path.exists(output_dir):
    os.makedirs(output_dir) # makedores builds the whole path, even nested folders!
    print(f"Directory {output_dir} was created.")
else:
    print("Directory already there, proceeding to save data.")
#4 os.remove() is the AI's way of cleaning up files it no longer needs. It deletes a specified file from the system.
temp_file = os.path.join(output_dir, "temp_weights.h5")
# Simulate creating a temporary file
with open(temp_file, 'w') as f:
    f.write("Temporary model weights data...")  
print(f"\nCreated temporary file: {temp_file}")
# Now let's remove it   
try:
    os.remove(temp_file)
    print(f"Temporary file {temp_file} has been removed.")  
except FileNotFoundError:
    print("Temporary file not found, nothing to remove.")
except PermissionError:
    print("Permission denied to remove the temporary file.")    
