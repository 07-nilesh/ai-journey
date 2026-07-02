import math

def binomial_probability(n, k, p=0.5):
    combinations = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return combinations * (p ** k) * ((1 - p) ** (n - k))

def calculate_p_value(total_trials, successes, base_p=0.5):
    p_value = 0
    for k in range(successes, total_trials + 1):
        p_value += binomial_probability(total_trials, k, base_p)
    return p_value
total_trials = 10
successes = 8
result_p_value = calculate_p_value(total_trials, successes)
print(f"P-value for {successes} successes out of {total_trials} trials: {result_p_value:.4f}")

if result_p_value <= 0.05:
    print("Verdict: Reject the Null Hypothesis! This isn't luck, it's a significant result.")
else:    print("Verdict: Fail to reject the Null Hypothesis. The result is not statistically significant.")
