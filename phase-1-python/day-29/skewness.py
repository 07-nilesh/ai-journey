def calculate_skewness_kurtosis(data):
    n = len(data)
    mean = sum(data) / n
    
    # Calculate Variance and Standard Deviation first
    variance = sum((x - mean) ** 2 for x in data) / n # Using population for simplicity here
    std_dev = variance ** 0.5
    
    # Third Moment (Cubed) for Skewness
    skewness = sum(((x - mean) / std_dev) ** 3 for x in data) / n
    
    # Fourth Moment (Power of 4) for Kurtosis
    # Note: We often subtract 3 to get "Excess Kurtosis". 
    # A perfectly normal distribution has a kurtosis of 3.
    kurtosis = sum(((x - mean) / std_dev) ** 4 for x in data) / n
    excess_kurtosis = kurtosis - 3
    
    return skewness, excess_kurtosis

# Example 1: SBI Wait Times (Right-Skewed with outliers)
wait_times = [5, 10, 12, 15, 18, 20, 25, 45, 120, 180]
skew, kurt = calculate_skewness_kurtosis(wait_times)

print(f"Skewness: {skew:.2f} (Positive -> Right-Skewed)")
print(f"Excess Kurtosis: {kurt:.2f} (Positive -> Fat tails / Heavy Outliers)")