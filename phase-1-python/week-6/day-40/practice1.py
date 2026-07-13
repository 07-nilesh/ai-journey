from pathlib import Path
print(Path("spam","eggs","bacon")) # creates a Path object representing the path "spam/eggs/bacon"
print(str(Path("spam","eggs","bacon"))) # converts the Path object to a string, resulting in "spam/eggs/bacon"
print(Path("spam")/"eggs"/"bacon") # creates a Path object representing the path "spam/eggs/bacon" using the division operator

homeFolder = Path("C:/Users/YourUsername") # creates a Path object representing the home directory
subFolder = Path("spam","eggs","bacon") # creates a Path object representing the subdirectory "spam/eggs/bacon"
fullPath = homeFolder / subFolder # combines the home directory and subdirectory into a full
print(fullPath) # prints the full path, which will be "C:/Users/YourUsername/spam/eggs/bacon"

import os
print(Path.cwd()) # prints the current working directory
print(Path.home()) # prints the home directory of the current user
#os.chdir("N:\AI\phase-1-python\day-40") # changes the current working directory to "N:\AI\phase-1-python\day-40"
print(Path.cwd()) # prints the new current working directory after changing it to "N:\AI\phase-1-python"

#os.makedirs("N:/AI/phase-1-python/day-40/made_folder") # creates a new directory called "some_folder" in the specified path
print("Directory created successfully.")

print(Path.cwd().is_absolute()) # checks if the current working directory is an absolute path, which should return True
print(Path.cwd() / Path("spam/eggs/bacon")) # combines the current working directory with the relative path "spam/eggs/bacon" to create a new Path object representing the full path to that location

print(os.path.abspath("spam/eggs/bacon")) # returns the absolute path of the relative path "spam/eggs/bacon" based on the current working directory
print(os.path.isabs("spam/eggs/bacon")) # checks if the path "spam/eggs/bacon" is an absolute path, which should return False since it's a relative path
print(os.path.relpath("spam/eggs/bacon", "day-40")) # returns the relative path of "spam/eggs/bacon" from the current working directory

p = Path('C:/Users/Al/spam.txt')
print(p.exists()) # checks if the file "spam.txt" exists at the specified path, which should return True if it does exist
print(p.anchor) # returns the anchor of the path, which is the part of the path that identifies the root directory (e.g., "C:/")
print(p.parent) # returns the parent directory of the path, which is "C:/Users/Al"
print(p.name) # returns the name of the file, which is "spam.txt"
print(p.stem) # returns the stem of the file name, which is "spam"
print(p.suffix) # returns the suffix of the file name, which is ".txt"
print(p.drive) # returns the drive letter of the path, which is "C:"

print(Path.cwd().parent) # returns the parent directory of the current working directory
print(Path.cwd().parents[0]) # returns the parent directory of the current working directory (same as above)
print(Path.cwd().parents[1]) # returns the grandparent directory of the current working directory

calcFilePath = "C:/Users/Al/spam.txt"
print(os.path.basename(calcFilePath)) # returns the base name of the file, which is "spam.txt"
print(os.path.dirname(calcFilePath)) # returns the directory name of the file, which is "C:/Users/Al"
print(os.path.split(calcFilePath)) # splits the path into a tuple containing the directory and the file name, which is ("C:/Users/Al", "spam.txt")
print(calcFilePath.split(os.sep)) # splits the path into a list of its components based on the path separator, which is ["C:", "Users", "Al", "spam.txt"]

#finding file size and listing directory contents
print(os.path.getsize(Path.cwd() / "spam.txt")) # returns the size of the file "spam.txt" in bytes
print(os.listdir(Path.cwd())) # returns a list of the names of the entries in the current working directory

totalSize = 0
for filename in os.listdir(Path.cwd()):
    totalSize += os.path.getsize(Path.cwd() / filename) # adds the size of each file in the current working directory to the total size
print(f"Total size of all files in the current directory: {totalSize} bytes")

#Modifying a List of Files Using Glob Patterns
p=Path.cwd()
for file in p.glob('*.txt'): # iterates through all files in the current directory that match the glob pattern '*.txt' (i.e., all text files)
    print(file) # prints the name of each text file found in the current directory
print(list(p.glob('*.txt'))) # creates a list of all text files in the current directory and prints it
print(list(p.glob('spam?.txt'))) # creates a list of all files in the current directory that match the glob pattern '*.?xt' (i.e., files with a single character extension followed by 'xt') and prints it

#Checking Path Validity
path = Path("C:/Users/Al/spam.txt")
path1=Path("N:\AI\phase-1-python\day-40")
print(path.exists()) # checks if the path "C:/Users/Al/spam.txt" exists, which should return True if the file exists at that location
print(path1.exists()) # checks if the path "N:\AI\phase-1-python\day-40" exists, which should return True since it appears to be an valid path
print(path.is_file()) # checks if the path "C:/Users/Al/spam.txt" is a file, which should return True if it is indeed a file
print(path.is_dir()) # checks if the path "C:/Users/Al/spam.txt" is a directory, which should return False since it is a file
print(path1.is_dir()) # checks if the path "N:\AI\phase-1-python\day-40" is a directory, which should return True if it is indeed a directory   
print(path1.is_file()) # checks if the path "N:\AI\phase-1-python\day-40" is a file, which should return False since it is a directory

drive = Path("C:/")
print(drive.is_dir()) # checks if the path "C:/" is a directory,