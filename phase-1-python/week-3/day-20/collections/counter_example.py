from collections import Counter

print(Counter("mississippi"))
## Update the counts of m and i
letters = Counter("mississippi")
letters.update(m=3, i=4)
print(letters)

# Add a new key-count pair
letters.update({"a": 2})
print(letters)

# Update with another counter
letters.update(Counter(["s", "s", "p"]))
print(letters)

multiset = Counter([1, 1, 2, 3, 3, 3, 4, 4])
print(multiset)
print(multiset.keys() == {1, 2, 3, 4})

inventory = Counter(dogs=23, cats=14, pythons=7)

adopted = Counter(dogs=2, cats=5, pythons=1)
inventory.subtract(adopted)
print(inventory)
# Counter({'dogs': 21, 'cats': 9, 'pythons': 6})

new_pets = {"dogs": 4, "cats": 1}
inventory.update(new_pets)
print(inventory)
# Counter({'dogs': 25, 'cats': 10, 'pythons': 6})

inventory = inventory - Counter(dogs=2, cats=3, pythons=1)
print(inventory)
# Counter({'dogs': 23, 'cats': 7, 'pythons': 5})

new_pets = {"dogs": 4, "pythons": 2}
inventory += new_pets
print(inventory)