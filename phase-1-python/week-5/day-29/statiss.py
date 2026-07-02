def full_stats(data):
    if not data:
        return None
    
    # Step 1: Sort the data for median calculation
    sorted_data = sorted(data)
    
    # Step 2: Calculate Mean
    mean = sum(data) / len(data)
    
    # Step 3: Calculate Median
    n = len(sorted_data)
    mid_index = n // 2
    if n % 2 == 0:
        median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
    else:
        median = sorted_data[mid_index]
    
    # Step 4: Calculate Mode
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    mode = modes[0] if len(modes) == 1 else modes

    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    sd= variance ** 0.5
    
    return {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': variance,
        'standard_deviation': sd
    }
data = [3.3, 3.3, 3.3, 3.5, 3.2, 3.4, 150.0]
stats = full_stats(data)
print(f"Mean: {stats['mean']:.2f} LPA")
print(f"Median: {stats['median']} LPA") 
print(f"Mode: {stats['mode']} LPA")
print(f"Variance: {stats['variance']:.2f}")
print(f"Standard Deviation: {stats['standard_deviation']:.2f} LPA")