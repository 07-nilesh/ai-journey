import itertools
'''
speakers = ["Nilesh", "Mohit", "Arjun"]

# Get all possible speaking orders (arranging all 3)
speaking_orders = itertools.permutations(speakers)

print("Possible speaking sequences:")
for order in speaking_orders:
    print(" -> ".join(order)) 

# If only 2 speak, we specify r=2
print("\nPossible pairs if only two speakers are chosen:")
pairs = itertools.permutations(speakers, 2)
for p in pairs:
    print(p) '''
finalists=["Team A", "Team B", "Team C", "Team D"]
prize_orders=itertools.permutations(finalists, 3)
print("Possible prize distributions (Gold, Silver, Bronze):")
for order in prize_orders:
    print(" -> ".join(order)) 