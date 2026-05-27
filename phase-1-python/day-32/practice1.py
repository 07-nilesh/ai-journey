import numpy as np
import matplotlib.pyplot as plt

# 1. Generate random array data: y = 2x + noise
np.random.seed(42) # Keeps the random numbers identical every run
x_data = np.linspace(0, 10, 50) # 50 points spaced between 0 and 10
noise = np.random.normal(0, 1.0, 50) # Random noise centered at 0
y_data = 2 * x_data + noise # Target values

# 2. Initialize parameters
w = 0.0
b = 0.0
lr = 1.0
epochs = 100 # Let's train longer to watch convergence
loss_history = [] # Notepad to store loss at each step

# 3. The Optimization Loop
for step in range(epochs):
    # Compute predictions for ALL 50 points simultaneously (Vectorization!)
    y_pred = w * x_data + b
    
    # Compute loss (Mean Squared Error)
    loss = np.mean((y_pred - y_data) ** 2)
    loss_history.append(loss) # Save it to plot later
    
    # Compute average gradients across the whole batch
    w_gradient = 2 * np.mean((y_pred - y_data) * x_data)
    b_gradient = 2 * np.mean(y_pred - y_data)
    
    # Update parameters simultaneously
    w -= lr * w_gradient
    b -= lr * b_gradient

# 4. PLOT 1: Loss over iterations
plt.figure(figsize=(6, 3))
plt.plot(loss_history, color='purple', lw=2)
plt.title("Loss Over Iterations (MSE)")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 5. PLOT 2: Final regression line on the data data
plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, color='blue', alpha=0.7, label='Actual Data')
plt.plot(x_data, w * x_data + b, color='red', lw=3, label=f'Line: y = {w:.2f}x + {b:.2f}')
plt.title("Final Regression Fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()