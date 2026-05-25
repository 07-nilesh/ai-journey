import matplotlib.pyplot as plt
import math

# A helper function to calculate the exact Poisson probability
def poisson_prob(k, lam):
    # The formal math formula: (e^(-lambda) * lambda^k) / k!
    return (math.exp(-lam) * (lam**k)) / math.factorial(k)

# Our different average rates (Lambda)
lam_values = [1, 5, 10]

plt.figure(figsize=(15, 5))

for i, lam in enumerate(lam_values):
    # x_values: Let's check the probability of getting anywhere from 0 to 20 calls
    x_values = list(range(21))
    
    # y_values: Calculate the probability for each exact number of calls
    y_values = [poisson_prob(k, lam) for k in x_values]
    
    # Plot as a bar chart (because calls are whole numbers/discrete!)
    plt.subplot(1, 3, i + 1)
    plt.bar(x_values, y_values, color='teal', edgecolor='black')
    
    plt.title(f'Poisson Distribution (λ = {lam})')
    plt.xlabel('Number of Events (k)')
    plt.ylabel('Probability')
    
    # Lock X and Y axes to make comparison fair
    plt.xlim(-1, 21)
    plt.ylim(0, 0.4)

plt.tight_layout()
plt.show()