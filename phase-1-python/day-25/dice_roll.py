import numpy as np
import matplotlib.pyplot as plt

# Set seed so we can compare our shapes
np.random.seed(42)

# 1. Roll two separate dice 10,000 times each
# Remember: randint is exclusive at the top boundary, so we use 7 to get 1-6!
die_1 = np.random.randint(1, 7, size=10000)
die_2 = np.random.randint(1, 7, size=10000)

# 2. Add the two massive arrays together element-wise (ufunc power!)
dice_sums = die_1 + die_2

# 3. Count how many times each sum (2 through 12) appeared
unique_sums, counts = np.unique(dice_sums, return_counts=True)

# Print the raw data to the terminal
print("Possible Sums: ", unique_sums)
print("Roll Counts:   ", counts)

# 4. Plot the distribution
plt.figure(figsize=(10, 6))

# We use a bar chart to show the exact count for each specific sum
bars = plt.bar(unique_sums, counts, color='#9b59b6', edgecolor='black')

plt.title('Distribution of 10,000 Two-Dice Rolls', fontsize=14)
plt.xlabel('Sum of Two Dice', fontsize=12)
plt.ylabel('Frequency of Roll', fontsize=12)

# Force the X-axis to show all numbers from 2 to 12 cleanly
plt.xticks(range(2, 13)) 

# Save the visualization
plt.savefig('dice_sum_distribution.png')
print("\nPlot saved successfully as 'dice_sum_distribution.png'!")