import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # stores the list of cats in the shelve file under the key 'cats'
shelfFile.close() # closes the shelve file to save the changes

shelfFile = shelve.open('mydata') # opens the shelve file 'mydata'
print(type(shelfFile)) # prints the type of the shelve file object
print(shelfFile['cats']) # retrieves and prints the list of cats stored under the key
print(list(shelfFile.keys())) # prints a list of all the keys in the shelve file
print(list(shelfFile.values())) # prints a list of all the values in the shelve file
shelfFile.close() # closes the shelve file to free up system resources

# Saving Variables with the pprint.pformat() Function
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats)) # prints a formatted string representation of the list of cats
fileObj = open('myCats.py', 'w') # opens a new file called 'myCats.py' in write mode
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') # writes a line to the file that assigns the formatted string representation of the list of cats to a variable called 'cats'
fileObj.close() # closes the file to save the changes

import myCats
print(myCats.cats) # imports the myCats module and prints the value of the cats