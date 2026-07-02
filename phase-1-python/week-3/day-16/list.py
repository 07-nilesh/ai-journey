# list comprehension
# 1. Basic transformation(squares of numbers)
squares = [x**2 for x in range(10)]
print(squares)

#2. Filtering (even numbers)
evens =[x for x in range(20) if x % 2 == 0]
print(evens)

#3. String manipulation (uppercase)
startups=["spotter","fitme","healthify"]
shouting_startups = [s.upper() for s in startups]
print(shouting_startups)

#4. Conditional Logic(if-else)
numbers = [1, 2, 3, 4, 5]
lables =["Even" if x%2==0 else "Odd" for x in numbers]
print(lables)

#5. Extracting specific elements (first letter of each word)
names=["Nilesh kashyap","David Malan","Andrej Karpathy"]
initials =[n.split()[0][0]+n.split()[1][0] for n in names]
print(initials)

#6. Filtering by String Length
words = ["AI", "Machine", "Learning", "Code", "Python"]
long_words = [w for w in words if len(w) > 5]
print(long_words)

#7. Flattening a Matrix (Nested Loops)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

#8. Mathematical Functions
celsius = [0, 10, 20, 30]
fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print(fahrenheit)

#9. Removing Vowels from a String
text = "Arya is your AI Tutor"
no_vowels = "".join([char for char in text if char.lower() not in "aeiou"])
print(no_vowels)

#10. File Path Processing
files = ["data.csv", "notes.txt", "summary.csv", "script.py"]
csv_only = [f for f in files if f.endswith(".csv")]
print(csv_only)