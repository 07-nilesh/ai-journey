import numpy as np
import matplotlib.pyplot as plt # Importing our plotting library

# 1. Simulate 10,000 coin flips instantly (0 = Tails, 1 = Heads)
# We use max boundary '2' because randint is exclusive at the top!
flips = np.random.randint(0, 2, size=10000)

# 2. Count the results using NumPy conditional sums
heads_count = np.sum(flips == 1)
tails_count = np.sum(flips == 0)

print(f"Total Heads: {heads_count}")
print(f"Total Tails: {tails_count}")

# 3. Plot the distribution
labels = ['Tails', 'Heads']
counts = [tails_count, heads_count]

plt.figure(figsize=(8, 6)) # Set the canvas size
plt.bar(labels, counts, color=['#e74c3c', '#3498db'])
plt.title('Distribution of 10,000 Coin Flips')
plt.ylabel('Number of Occurrences')

# Save the plot
plt.savefig('coin_flip_distribution.png')