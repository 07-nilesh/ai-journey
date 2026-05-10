import itertools
team_alpha = ["Alice", "Bob", "Charlie"]
team_beta = ["David", "Eve", "Frank"]
all_teams=itertools.chain(team_alpha, team_beta)
print(list(all_teams))  # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
print("All team members:")
for member in all_teams:
    print(f"Welcome, {member}!")