import os
for foldername, subfolder, filenames in os.walk(os.getcwd()):
    print(f"The current folder is {foldername}")
    print("The subfolders in " + foldername + " are: " + str(subfolder))
    print("The filenames in " + foldername + " are: " + str(filenames))
    print()