
#1
sentences = ["I love coding in Python", "Machine Learning is the future", "Indore is a clean city"]
word_filter=[word for sentence in sentences for word in sentence.split() if len(word)>5]
print(word_filter)

#2
members = [
    {"name": "Nilesh", "age": 22},
    {"name": "Arya", "age": 28},
    {"name": "Rahul", "age": 30},
    {"name": "Sonia", "age": 19}
]
adults={member["name"]: member["age"] for member in members if member["age"]>=25}
print(adults)