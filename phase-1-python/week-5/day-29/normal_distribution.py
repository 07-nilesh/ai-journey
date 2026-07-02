# Constants
PI = 3.1415926535
E = 2.7182818284

def normal_pdf(x, mean, std_dev):
    """
    Calculates the Probability Density of a normal distribution 
    at a specific point 'x'.
    """
    variance = std_dev ** 2
    
    # Part 1: The scaling factor (the fraction outside the e)
    scale_factor = 1 / ((2 * PI * variance) ** 0.5)
    
    # Part 2: The exponent of e
    exponent = -((x - mean) ** 2) / (2 * variance)
    
    # Final calculation
    probability_density = scale_factor * (E ** exponent)
    
    return probability_density

# Example: Zomato delivery with Mean = 30 mins, Std Dev = 5 mins
x_val = 30 # Let's check the density right at the mean
density = normal_pdf(x_val, mean=30, std_dev=5)

print(f"Density at exactly {x_val} mins: {density:.4f}")

# You would loop this function over many x values (e.g., from 10 to 50) 
# to plot the actual bell curve graph!