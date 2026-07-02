import numpy as np

current_weight = np.array([2.0,1.0,1.0])# Initial weight vector

def compute_gradient(weight):
    x=weight[0]
    y=weight[1]
    z=weight[2]
    grad_x=2*x # Partial derivative with respect to x
    grad_y=6*y # Partial derivative with respect to y
    grad_z=8*z # Partial derivative with respect to z
    return np.array([grad_x, grad_y, grad_z])
gradient_vector = compute_gradient(current_weight)
lr = 0.1 # Learning rate
new_weight = current_weight - (lr * gradient_vector) # Update weight vector
print("Current weight:", current_weight)
print("New weight:", new_weight)
print("Gradient:", gradient_vector)

#variation 2
import numpy as np

current_weight = np.array([0.0,1.0])# Initial weight vector

def compute_gradient(weight):
    x=weight[0]
    y=weight[1]
    
    grad_x=2*x # Partial derivative with respect to x
    grad_y=-6*y # Partial derivative with respect to y
    return np.array([grad_x, grad_y])
gradient_vector = compute_gradient(current_weight)
lr = 0.1 # Learning rate
new_weight = current_weight - (lr * gradient_vector) # Update weight vector
print("Current weight:", current_weight)
print("New weight:", new_weight)
print("Gradient:", gradient_vector)