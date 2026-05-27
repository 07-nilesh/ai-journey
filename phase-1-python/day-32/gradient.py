current_weight = 10.0 # Initial weight
lr = 0.1 # Learning rate

for step in range(10):
    gradient = 2 * current_weight # Derivative of f(w) = w^2 is f'(w) = 2w
    current_weight -= lr * gradient # Update weight
    loss = current_weight ** 2 # Loss is f(w) = w^2
    print(f"Step {step+1}: Weight = {current_weight:.4f}, Loss = {loss:.4f}")

'''
# variation 1
current_weight = 10.0 # Initial weight
lr = 0.1 # Learning rate

for step in range(10):
    gradient = 2 * (current_weight - 7) # Derivative of f(w) = (w - 7)^2 is f'(w) = 2(w - 7)
    current_weight -= lr * gradient # Update weight
    loss = (current_weight - 7) ** 2 # Loss is f(w) = (w - 7)^2
    print(f"Step {step+1}: Weight = {current_weight:.4f}, Loss = {loss:.4f}")


# variation 2
current_weight = 10.0 # Initial weight
lr = 0.1 # Learning rate

step_count = 0
while abs(current_weight) > 0.001: # Continue until weight is close enough to 0
    step_count += 1
    gradient = 2 * current_weight # Derivative of f(w) = w^2 is f'(w) = 2w
    current_weight -= lr * gradient # Update weight
    loss = current_weight ** 2 # Loss is f(w) = w^2
    print(f"Step {step_count}: Weight = {current_weight:.4f}, Loss = {loss:.4f}")
'''