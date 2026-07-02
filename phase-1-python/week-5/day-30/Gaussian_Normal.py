import matplotlib.pyplot as plt
import numpy as np
import math

# A helper function to calculate the exact Gaussian curve (Probability Density)
def gaussian_prob(x, mu, sigma):
    # The formal math formula for the Bell Curve
    coefficient = 1.0 / (sigma * math.sqrt(2 * math.pi))
    exponent = math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return coefficient * exponent

# Generate 1000 smoothly spaced X values from -10 to +10
x_values = np.linspace(-10, 10, 1000)

# Define our three scenarios: (Mean, Standard Deviation, Color, Label)
scenarios = [
    (0, 1, 'blue', 'Standard (μ=0, σ=1)'),
    (0, 2, 'orange', 'Wide (μ=0, σ=2)'),
    (3, 1, 'green', 'Shifted (μ=3, σ=1)')
]

plt.figure(figsize=(10, 6))

# Loop through each scenario and plot it on the same canvas
for mu, sigma, color, label in scenarios:
    # Calculate the Y values (height of the curve) for every X
    y_values = [gaussian_prob(x, mu, sigma) for x in x_values]
    
    # Plot as a smooth line instead of bars
    plt.plot(x_values, y_values, color=color, label=label, linewidth=2.5)

plt.title('Gaussian / Normal Distributions')
plt.xlabel('Value (X)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()