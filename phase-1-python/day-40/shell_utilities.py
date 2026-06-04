import shutil, os
from pathlib import Path
p=Path.cwd()
'''
      ----- copying files and directories -----
# 1.copy file from current directory to some_folder
shutil.copy(p/'spam.txt', p/'some_folder') #copies spam.txt to some_folder with the same name
print("File copied successfully!")

# 2.copy file and rename it in the process
shutil.copy(p / 'eggs.txt', p / 'some_folder' / 'eggs2.txt') #copies eggs.txt to some_folder and renames it to eggs2.txt
print("File copied and renamed successfully!")

# 3.copy entire directory and its contents to some_folder
shutil.copytree(p / 'my_folder', p / 'some_folder' / 'my_folder_copy')#copies my_folder and all its contents to some_folder and renames it to my_folder_copy
print("Directory copied successfully!")

       ----- moving files and directories -----
# 4.move file from current directory to some_folder
shutil.move(p / 'move_file.txt', p / 'some_folder' / 'move_file.txt') #moves move_file.txt to some_folder with the same name
print("File moved successfully!")

#5.move and rename file in the process
shutil.move(p/'eggs.txt', p/'some_folder'/'new_eggs.txt') #moves eggs.txt to some_folder and renames it to new_eggs.txt
print("File moved and renamed successfully!")

#6.move file to a new location and rename it
shutil.move(p/'bacon.txt', p/'eggs') #moves bacon.txt to eggs directory and renames it to bacon.txt
print("File moved to new location and renamed successfully!")

         ----- deleting files and directories -----

#7. checking which .txt files would be deleted if we uncomment the unlink() line above
for file in p.glob('*.txt'):
    #file.unlink()
    print(f"{file} will be deleted if you uncomment the unlink() line above!")

#8.delete a file
for file in p.glob('*.rxt'): # deletes all .rxt files in the current directory
    file.unlink()
    print(f"{file} deleted successfully!")
'''
import send2trash
baconFile = open(p / 'bacon.txt', 'a') #opens bacon.txt in append mode, creating it if it doesn't exist
baconFile.write("Bacon is not a vegetable.") #writes a line to bacon.txt
baconFile.close()
send2trash.send2trash(p / 'bacon.txt') #sends bacon.txt to the recycle bin instead of permanently deleting it
print("File sent to recycle bin successfully!")