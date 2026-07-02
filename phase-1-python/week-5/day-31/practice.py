
def gradient(func,x,h_step=0.001):
    y_now=func(x)
    y_later=func(x+h_step)
    slope=(y_later-y_now)/h_step
    return slope

simple_func=lambda x: 3*(x**2)+2*x+1
x=4.0
result=gradient(simple_func,x)
print(f"Approximate derivative (gradient) at x={x}: {result:.4f}")