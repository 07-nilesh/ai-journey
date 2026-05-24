def calculate_quartiles_iqr(data):
    if not data or len(data) < 4:
        return "Need at least 4 data points"
        
    # Step 1: Always sort the data
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # Helper function to find median
    def get_median(lst):
        l = len(lst)
        mid = l // 2
        return (lst[mid - 1] + lst[mid]) / 2 if l % 2 == 0 else lst[mid]

    # Step 2: Find Q2 (Overall Median)
    q2 = get_median(sorted_data)
    
    # Step 3: Split into halves
    mid_index = n // 2
    lower_half = sorted_data[:mid_index]
    # If odd length, skip the exact middle element for the upper half
    upper_half = sorted_data[mid_index + (1 if n % 2 != 0 else 0):]
    
    # Step 4: Find Q1 and Q3
    q1 = get_median(lower_half)
    q3 = get_median(upper_half)
    
    # Step 5: Calculate IQR and Outlier limits
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    
    # Check for actual outliers in the data
    outliers = [x for x in sorted_data if x < lower_bound or x > upper_bound]
    
    return {
        "Q1": q1, "Q2 (Median)": q2, "Q3": q3,
        "IQR": iqr, "Outlier Bounds": (lower_bound, upper_bound),
        "Detected Outliers": outliers
    }

# Example: SECR Train Delays (in minutes) with one crazy 5-hour delay!
delays = [5, 10, 12, 15, 20, 22, 25, 30, 35, 300]

results = calculate_quartiles_iqr(delays)
for key, value in results.items():
    print(f"{key}: {value}")