import os
from pathlib import Path
p = Path("spam.txt")
p.write_text("Hello, world!") # creates a new file called "spam.txt" and writes the string "Hello, world!" to it
print(p.read_text()) # reads the contents of "spam.txt" and prints it to the console

# Opening Files with the open() Function
helloFile = open(Path.cwd() / "hello.txt") # opens the file "hello.txt" in the current working directory and assigns it to the variable helloFile
helloContent = helloFile.read() # reads the contents of helloFile and assigns it to the variable helloContent
content_lines = helloFile.readlines() # reads the contents of helloFile and returns it as a list of lines, which is assigned to the variable content_lines
print(helloContent) # prints the contents of helloFile to the console
print(content_lines) # prints the list of lines to the console

helloFile.close() # closes the file helloFile to free up system resources

baconFile = open(Path.cwd() / "bacon.txt", 'w') # opens the file "bacon.txt" in write mode, creating it if it doesn't exist
baconFile.write("Hello, world!\n") # writes the string "Hello, world!" followed by a newline character to baconFile
baconFile.close() # closes the file baconFile to save the changes

baconFile = open(Path.cwd() / "bacon.txt", 'a') # opens the file "bacon.txt" in append mode, allowing new content to be added without overwriting existing content
baconFile.write("Bacon is not a vegetable.") # writes the string "Bacon is not a vegetable." to baconFile, adding it to the end of the file
baconFile.close() # closes the file baconFile to save the changes

baconFile = open(Path.cwd() / "bacon.txt") # opens the file "bacon.txt" in read mode
content = baconFile.read() # reads the contents of baconFile and assigns it to the variable
print(content) # prints the contents of baconFile to the console
baconFile.close() # closes the file baconFile to free up system resources