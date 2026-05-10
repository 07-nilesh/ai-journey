from collections import defaultdict
'''
pets = [
    ("dog", "Affenpinscher"),
    ("dog", "Terrier"),
    ("dog", "Boxer"),
    ("cat", "Abyssinian"),
    ("cat", "Birman"),
    ] 

group_pets = defaultdict(list)

for pet, breed in pets:
    group_pets[pet].append(breed)


for pet, breeds in group_pets.items():
    print(pet, "->", breeds)
'''

marks=defaultdict(int)
marks["DSA"]=10
marks["java"]=15
if marks["DSA"]==10:
    marks["DSA"]+=5

total_marks=0
for sub,mark in marks.items():
    total_marks+=mark
print(marks)
print("Total marks:", total_marks)
