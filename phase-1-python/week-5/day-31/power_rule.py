x=4.0
tiny_step=0.0001
y_now=x**3
y_later=(x+tiny_step)**3
roc=(y_later-y_now)/tiny_step
print(f"Approximate derivative (rate of change) at x={x}: {roc:.4f}")

exact_derivative=3*(x**2)
print(f"Exact derivative at x={x}: {exact_derivative:.4f}")

# Variation 1
x=4.0
derivative_1=3*(x**2)
derivative_2=2*x
exact_derivative=derivative_1+derivative_2
print(f"Exact derivative at x={x} for f(x)=x^3+x^2: {exact_derivative:.4f}")

# Variation 2
x=3.0
u=x**2
y=u**3
# first slope
slope_1=2*x
# second slope
slope_2=3*(u**2)
#apply chain rule
exact_derivative=slope_1*slope_2
print(f"Exact derivative at x={x} : {exact_derivative:.4f}")
