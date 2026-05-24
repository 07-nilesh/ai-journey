def calculate_median(data):
    if not data: return None
    
    # Step 1: Always sort the data first!
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid_index = n // 2
    
    # Step 2: Check if even or odd length
    if n % 2 == 0:
        # If even, average the two middle numbers
        return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
    else:
        # If odd, just take the exact middle number
        return sorted_data[mid_index]

def calculate_mode(data):
    if not data: return None
    
    # Step 1: Count frequencies
    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1
        
    # Step 2: Find the maximum count
    max_count = max(counts.values())
    
    # Step 3: Find all items that have that maximum count
    modes = [k for k, v in counts.items() if v == max_count]
    
    # Return single value if one mode, else return list of modes
    return modes[0] if len(modes) == 1 else modes

# Example: Tech Park Salaries (in LPA) with an outlier
salaries = [3.3, 3.3, 3.3, 3.5, 3.2, 3.4, 150.0]

print(f"Mean: {sum(salaries)/len(salaries):.2f} LPA") # Gets pulled up massively
print(f"Median: {calculate_median(salaries)} LPA")   # Stays stable
print(f"Mode: {calculate_mode(salaries)} LPA")       # The most common