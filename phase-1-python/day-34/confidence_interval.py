import math

def calculate_CI(data, confidence=0.95):
    mean = sum(data) / len(data)
    std_dev = math.sqrt(sum([(x - mean) ** 2 for x in data]) / (len(data) - 1))
    z_score = 1.96  # For 95% confidence
    margin_of_error = z_score * (std_dev / math.sqrt(len(data)))
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return lower_bound, upper_bound, mean
data=[10,10,10,10]
sample_data = [10, 12, 14, 18, 20, 22, 24]
large_sample_data = [10, 12, 14, 18, 20, 22, 24] * 10
ci_lower, ci_upper, sample_mean = calculate_CI(sample_data)
print(f"Sample Mean: {sample_mean}")
print(f"95% Confidence Interval: [{ci_lower:.2f}, {ci_upper:.2f}]")
