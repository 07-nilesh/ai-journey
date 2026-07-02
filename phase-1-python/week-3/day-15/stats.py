def stats_summary(*numbers):
    mean = sum(numbers) / len(numbers)
    median = sorted(numbers)[len(numbers) // 2]
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)  
    return {
        'mean': mean,
        'median': median,
        'variance': variance,
        'min': minimum,
        'max': maximum
    }
data = [10, 20, 30, 40, 50]
summary = stats_summary(*data)
print(summary)