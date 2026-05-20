import numpy as np
import matplotlib.pyplot as plt

# Set the seed for reproducibility
np.random.seed(42)

# 1. Define the experiment parameters
num_samples = 1000  # How many times we run the experiment
sample_size = 30    # How many dice we roll in each experiment

# 2. Simulate ALL 30,000 dice rolls instantly!
# We create a 2D matrix: 1000 rows (experiments) x 30 columns (dice)
all_rolls = np.random.randint(1, 7, size=(num_samples, sample_size))

# 3. Calculate the mean for EACH row (axis=1 means "across the columns")
# This collapses our 1000x30 matrix into a 1D array of 1000 averages
sample_means = np.mean(all_rolls, axis=1)

# Print the first 5 averages to see what they look like
print("First 5 sample means:", np.round(sample_means[:5], 2))

# 4. Plot the distribution of the 1000 averages
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, color='#2ecc71', edgecolor='black', alpha=0.7)
plt.title(f'Central Limit Theorem: {num_samples} Means of {sample_size} Dice', fontsize=14)
plt.xlabel('Average Value of 30 Dice', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

# Save the plot
plt.savefig('clt_simulation.png')
print("\nPlot saved successfully as 'clt_simulation.png'!")