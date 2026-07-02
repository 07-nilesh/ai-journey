#1 Simple Mapping (Squares)
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)

#2 Character Counting (Frequency)
word = "indore"
char_freq = {char: word.count(char) for char in word}
print(char_freq)

#3. Filtering a Dictionary
startups = {"Spotter": 50, "FitMe": 5, "Healthify": 120}
unicorns = {k: v for k, v in startups.items() if v > 100}
print(unicorns)

#4. Merging Two Lists into a Dictionary
users = ["Nilesh", "David", "Arya"]
roles = ["Founder", "Professor", "AI Tutor"]
user_roles = {user: role for user, role in zip(users, roles)}
print(user_roles)

#5. Swapping Keys and Values
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)