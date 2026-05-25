import matplotlib.pyplot as plt

# 1. Define our different parameters (probabilities of success)
p_values = [0.20, 0.50, 0.80]

# The only two possible outcomes in Bernoulli
outcomes = ['Failure (0)', 'Success (1)']

# Set up a wide figure to hold 3 subplots side-by-side
plt.figure(figsize=(12, 4))

for i, p in enumerate(p_values):
    # Calculate probability of failure
    prob_failure = 1 - p
    
    # Store the probabilities to plot
    probs = [prob_failure, p]
    
    # Create a subplot for each 'p' value
    plt.subplot(1, 3, i + 1)
    
    # Plot the bars
    plt.bar(outcomes, probs, color=['salmon', 'skyblue'])
    
    # Lock the Y-axis from 0 to 1 so we can compare them fairly
    plt.ylim(0, 1)
    
    # Add labels
    plt.title(f'Bernoulli Distribution (p = {p})')
    plt.ylabel('Probability')

# Adjust layout so they don't overlap
plt.tight_layout()
plt.show()