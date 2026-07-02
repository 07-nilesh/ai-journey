import numpy as np

# --- Part 1: Median & Percentile ---
# 10 normal salaries, and 1 massive CEO outlier
salaries = np.array([40, 42, 45, 50, 52, 55, 58, 60, 62, 65, 9000])

print("The Lying Average: $", np.round(np.mean(salaries), 2))
print("The True Median:   $", np.median(salaries))

# Find the 25th and 75th percentiles (The Interquartile Range)
p_25 = np.percentile(salaries, 25)
p_75 = np.percentile(salaries, 75)
print(f"Bottom 25% make less than: ${p_25}")
print(f"Top 25% make more than:    ${p_75}\n")


# --- Part 2: Covariance & Correlation ---
# Let's say these are 5 students. 
hours_studied = np.array([1, 2, 3, 4, 5])
test_scores   = np.array([60, 65, 75, 85, 95])

# Calculate Covariance (Messy, unscaled relationship)
covariance_matrix = np.cov(hours_studied, test_scores)
print("Covariance Matrix:\n", covariance_matrix)

# Calculate Correlation (Clean, scaled relationship between -1 and 1)
correlation_matrix = np.corrcoef(hours_studied, test_scores)
print("\nCorrelation Matrix:\n", np.round(correlation_matrix, 2))

# Extract the specific score between Hours and Tests
actual_correlation = correlation_matrix[0, 1]
print(f"\nFinal Correlation Score: {np.round(actual_correlation, 2)} (Extremely strong positive relationship!)")

#2 practice
response_times = np.array([12, 15, 14, 18, 12, 16, 13, 15, 900, 14, 17, 15])
a=np.percentile(response_times, 5)
b=np.percentile(response_times, 95)
print(f"5th Percentile: {a}")
print(f"95th Percentile: {b}")
# Instantly keep only the healthy server responses!
clean_data = response_times[response_times < b] 
print(clean_data) 
# Output: [12 15 14 18 12 16 13 15 14 17 15] (The 900 is permanently gone!)