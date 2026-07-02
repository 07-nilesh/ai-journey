def create_probability_distribution(data):
    if not data:
        return {}
        
    total_observations = len(data)
    counts = {}
    
    # Step 1: Count the frequencies (just like a histogram!)
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            
    # Step 2: Convert counts to probabilities
    probability_distribution = {}
    for outcome, count in counts.items():
        # Probability = (Count of outcome) / (Total observations)
        probability_distribution[outcome] = count / total_observations
        
    return probability_distribution

# Example: Number of server errors logged per day over 10 days
daily_errors = [0, 1, 0, 0, 2, 1, 0, 3, 0, 1]

# Generate the distribution
dist = create_probability_distribution(daily_errors)

print("Discrete Probability Distribution:")
for outcome in sorted(dist.keys()):
    print(f"P({outcome} errors) = {dist[outcome]:.2f} (or {dist[outcome]*100:.0f}%)")

# Verify that all probabilities sum to 1
total_prob = sum(dist.values())
print(f"\nTotal Probability Sum: {total_prob:.2f}")