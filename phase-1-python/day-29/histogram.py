def create_histogram(data, num_bins):
    if not data:
        return {}
        
    min_val, max_val = min(data), max(data)
    # Add a tiny amount to max_val so the highest number doesn't get left out
    bin_width = (max_val - min_val + 0.0001) / num_bins
    
    # Initialize our bins with a count of 0
    # Dictionary keys will be the start of the bin
    histogram = {round(min_val + i * bin_width, 2): 0 for i in range(num_bins)}
    
    # Sort data into bins
    for value in data:
        # Find which bin index this value belongs to
        bin_index = int((value - min_val) // bin_width)
        bin_start = round(min_val + bin_index * bin_width, 2)
        histogram[bin_start] += 1
        
    return histogram

# Example: DSA Marks for 15 students out of 100
dsa_marks = [12, 45, 48, 52, 55, 61, 65, 68, 72, 75, 78, 85, 88, 92, 95]

hist_data = create_histogram(dsa_marks, num_bins=4)

print("Histogram Frequencies (Bin Start : Count)")
for bin_start, count in hist_data.items():
    # Printing a visual ASCII representation
    print(f"{bin_start:05.2f}+ | {'█' * count} ({count})")