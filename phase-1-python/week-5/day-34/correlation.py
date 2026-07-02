import math

indore_temperature = [30, 32, 28, 31, 29,100]
tea_sales = [100, 120, 80, 110, 90, 5000]

def calculate_correlation(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    
    numerator =0
    sum_x_squared = 0
    sum_y_squared = 0
    for i in range(len(x)):
       diff_x = x[i] - mean_x
       diff_y = y[i] - mean_y
       numerator += diff_x * diff_y

       sum_x_squared += diff_x ** 2
       sum_y_squared += diff_y ** 2

    denominator = math.sqrt(sum_x_squared * sum_y_squared)
    if denominator == 0:
        return 0
    return numerator / denominator
def vectorized_correlation(x,y):
    mean_x= sum(x) / len(x)
    mean_y= sum(y) / len(y)

    diff_x = [val - mean_x for val in x]
    diff_y = [val - mean_y for val in y]
    numerator = sum([diff_x[i] * diff_y[i] for i in range(len(x))])
    sum_x_squared = sum([d ** 2 for d in diff_x])
    sum_y_squared = sum([d ** 2 for d in diff_y])
    denominator = math.sqrt(sum_x_squared * sum_y_squared)
    if denominator == 0:
        return 0
    return numerator / denominator

correlation = calculate_correlation(indore_temperature, tea_sales)
vectorized_correlation = vectorized_correlation(indore_temperature, tea_sales)
print("Correlation:", correlation)
print("Vectorized Correlation:", vectorized_correlation)