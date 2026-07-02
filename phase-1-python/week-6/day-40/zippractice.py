import zipfile, os
from pathlib import Path
p = Path.cwd()

exampleZip = zipfile.ZipFile(p / 'campusgrid.zip') # opens the example.zip file
print("The names of the files in the zip file are: " + str(exampleZip.namelist())) # prints the names of the files in the zip file
spamInfo = exampleZip.getinfo('Phase-1/Role 2 Execution Map.docx') # gets information about the spam.txt file in the zip file
print(f"Size of {spamInfo.filename}: {spamInfo.file_size} bytes")
spamInfo.compress_size # gets the compressed size of the file in the zip file
print(f"Compressed size of {spamInfo.filename}: {spamInfo.compress_size} bytes")
print(f'Compressed file is {round(spamInfo.file_size / spamInfo
.compress_size, 2)}x smaller!') # calculates and prints how much smaller the compressed file is compared to the original file
exampleZip.close() # closes the zip file
'''
#2. extracting files from a zip file
exampleZip = zipfile.ZipFile(p / 'campusgrid.zip') # opens the example.zip file
exampleZip.extractall()
exampleZip.close()
print("Files extracted successfully!")
'''
newZip = zipfile.ZipFile(p / 'new.zip', 'w') # creates a new zip file called new.zip in write mode
newZip.write( 'spam.txt', compress_type=zipfile.ZIP_DEFLATED) # adds spam.txt to the new zip file with compression

newZip.close() # closes the new zip file

exampleZip = zipfile.ZipFile(p / 'new.zip') # opens the example.zip file
print("The names of the files in the zip file are: " + str(exampleZip.namelist()))