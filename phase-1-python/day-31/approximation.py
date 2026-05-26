# Approximation of Derivative (Rate of Change)
# We can use the concept of limits to approximate the derivative of a function at a specific point
def approximation(func,x ,h_step=0.001):
    #calculate the function value at x and x+h_step
    y_now=func(x)
    y_later=func(x+h_step)
    #calculate the slope (rate of change) using the difference quotient formula
    slope=(y_later-y_now)/h_step
    return slope
#function to test the approximation
def func(x):
    return x**3
#calculate the approximate derivative at x=4.0
result=approximation(func,4.0)
print(f"Approximate derivative (rate of change) at x=4.0: {result:.4f}")

# Variation 1
# Approximation of Derivative (Rate of Change)
# We can use the concept of limits to approximate the derivative of a function at a specific point
def approximation(func,x ,h_step=0.001):
    #calculate the function value at x and x+h_step
    y_now=func(x)
    y_later=func(x+h_step)
    #calculate the slope (rate of change) using the difference quotient formula
    slope=(y_later-y_now)/h_step
    return slope
#function to test the approximation
def func(x):
    return x**3
#calculate the approximate derivative at x=4.0
x=4.0
result=approximation(func,x)
exact_derivative=3*(x**2)
abs_difference=abs(result-exact_derivative)
print(f"Approximate derivative (rate of change) at x={x}: {result:.4f}")
print(f"Exact derivative at x={x}: {exact_derivative:.4f}")
print(f"Absolute difference: {abs_difference:.4f}")

# Variation 2
# Approximation of Derivative (Rate of Change)
# We can use the concept of limits to approximate the derivative of a function at a specific point
def approximation(func,h_step,x=4.0):
    #calculate the function value at x and x+h_step
    y_now=func(x)
    y_later=func(x+h_step)
    #calculate the slope (rate of change) using the difference quotient formula
    slope=(y_later-y_now)/h_step
    return slope
#function to test the approximation
def func(x):
    return x**3
#calculate the approximate derivative at x=4.0
result=approximation(func,h_step=2.0)
result_2=approximation(func,h_step=0.01)
result_3=approximation(func,h_step=1e-20)


print(f"Approximate derivative (rate of change) at x=4.0 with large step: {result:.4f}")
print(f"Approximate derivative (rate of change) at x=4.0 with medium step: {result_2:.4f}")
print(f"Approximate derivative (rate of change) at x=4.0 with microscopic step: {result_3:.4f}")