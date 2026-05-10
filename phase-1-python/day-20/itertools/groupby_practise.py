import itertools
'''
# Raw logs (Mixed order)
logs = [
    ("Chest", "Bench Press"),
    ("Back", "Pullups"),
    ("Chest", "Pushups"),
    ("Back", "Deadlift"),
    ("Chest", "Dips")
]

# 1. We MUST sort by the category (the first item in the tuple) first!
logs.sort() 

# 2. Group them by category
grouped_logs = itertools.groupby(logs, key=lambda x: x[0])

print("SPOTTER Workout Summary:")
for category, group in grouped_logs:
    # 'group' is an iterator, let's turn it into a list to see the items
    exercises = list(group)
    print(exercises)
    print(f"[{category}]: {len(exercises)} sets completed")
    for cat, ex in exercises:
        print(f"  - {ex}")
        '''
import itertools

text = "AAABBCDAA"

# 1. To group ALL identical characters together:
text_sorted = sorted(text) 
for char, group in itertools.groupby(text_sorted):
    print(f"Total {char} -> {len(list(group))}")

print("-" * 10)

# 2. To group only CONSECUTIVE characters (the default behavior):
for char, group in itertools.groupby(text):
    print(f"Streak of {char} -> {len(list(group))}")
