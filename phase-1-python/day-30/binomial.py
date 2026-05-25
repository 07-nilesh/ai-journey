import matplotlib.pyplot as plt
import math

def binomial_prob(n,k,p):
    combinations = math.comb(n, k)
    return combinations * (p ** k) * ((1 - p) ** (n - k))

n=20

p_values = [0.10, 0.50, 0.90]
plt.figure(figsize=(15, 5))
for i,p in enumerate(p_values):
    x_values = list(range(n + 1))
    y_values = [binomial_prob(n, k, p) for k in x_values]
    plt.subplot(1, 3, i + 1)
    plt.bar(x_values, y_values, color='mediumpurple', edgecolor='black')
    plt.title(f'Binomial Distribution (n={n}, p={p})')
    plt.xlabel('Number of Successes (k)')
    plt.ylabel('Probability')
    
    # Lock the x-axis so we can compare them fairly
    plt.xlim(-1, 21)

plt.tight_layout()
plt.show()