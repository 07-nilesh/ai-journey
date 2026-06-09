import itertools
'''
# Features for our "SPOTTER" gym app
features = ["Weight", "Height", "Age", "Heart_Rate"]

# Find all possible pairs (groups of 2) to test
feature_pairs = itertools.combinations(features, 2)

print("Possible unique pairs to analyze:")
for pair in feature_pairs:
    print(pair)

# Output will show 6 unique pairs like ('Weight', 'Height'), etc.
# Note: You won't see ('Height', 'Weight') because it's the same combination!
'''
participants = ["Alice", "Bob", "Charlie", "David"]
# We want to create unique teams of 3 for a group project
teams = itertools.combinations(participants, 3)

print("Possible unique teams:")
for team in teams:
    print(team)
