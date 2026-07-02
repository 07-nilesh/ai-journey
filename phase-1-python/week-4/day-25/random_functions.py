import numpy as np

# 1. THE SEED: Run this entire block multiple times. 
# Because the seed is locked to '42', the "random" numbers will NEVER change!
np.random.seed(42)

# 2. GENERATORS
flat_decimals = np.random.rand(3)       # 3 items, Uniform [0, 1)
bell_curve    = np.random.randn(3)      # 3 items, Normal (centered at 0)
whole_numbers = np.random.randint(1, 100, size=(2, 2)) # 2x2 grid between 1 and 99

print("Uniform (rand):   ", np.round(flat_decimals, 2))
print("Gaussian (randn): ", np.round(bell_curve, 2))
print("Integers (randint):\n", whole_numbers)


# 3. CHOICE
options = np.array(["Red", "Green", "Blue", "Yellow"])
# Pick 5 random colors, allowing the same color to be picked twice (replace=True)
selections = np.random.choice(options, size=5, replace=True)
print("\nRandom Choices:", selections)


# 4. SHUFFLE vs PERMUTATION
deck_A = np.array([10, 20, 30, 40, 50])
deck_B = np.array([10, 20, 30, 40, 50])

# Permutation (Safe/Out-of-place): Returns a NEW mixed array
new_mixed_deck = np.random.permutation(deck_A)
print("\n--- PERMUTATION ---")
print("Original Deck A remains safe: ", deck_A)
print("Newly created Mixed Deck:     ", new_mixed_deck)

# Shuffle (Destructive/In-place): Returns None, modifies the original instantly
np.random.shuffle(deck_B)
print("\n--- SHUFFLE ---")
print("Original Deck B is DESTROYED: ", deck_B)

#2 practice
np.random.seed(99)
A=np.arange(1,6)
print("Original Array:", A)
new_A=np.random.permutation(A)
print("Permuted Array:", new_A)