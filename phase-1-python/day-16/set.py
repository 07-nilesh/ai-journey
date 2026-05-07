#1. Unique Squares (Handling Duplicates)
numbers = [1, -1, 2, -2, 3, 3]
unique_squares = {x**2 for x in numbers}
print(unique_squares)

#2. Extracting Unique Categories
tags = ["Cardio", "Strength", "Cardio", "Yoga", "Strength", "HIIT"]
unique_tags = {t.lower() for t in tags}
print(unique_tags)

#3. Filtering Vowels from a Sentence
quote = "Success is not final, failure is not fatal"
vowels_present = {char.lower() for char in quote if char.lower() in 'aeiou'}
print(vowels_present)

#4. Finding Shared Elements (Intersection Logic)
members = ["Nilesh", "Arya", "Rahul"]
trainers = ["Rahul", "Sonia"]
member_trainers = {name for name in members if name in trainers}
print(member_trainers)

#5. Length of Unique Words
sentence = "Python is amazing and Python is fast"
lengths = {len(word) for word in sentence.split()}
print(lengths)