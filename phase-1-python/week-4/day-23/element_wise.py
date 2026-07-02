import numpy as np

# Create two identical 1D arrays
inventory_store_A = np.array([10, 20, 30, 40])
inventory_store_B = np.array([2,  5,  10, 4])

# 1. Element-wise Addition (+)
total_inventory = inventory_store_A + inventory_store_B
print("Addition Result:   ", total_inventory) # Output: [12, 25, 40, 44]

# 2. Element-wise Subtraction (-)
difference = inventory_store_A - inventory_store_B
print("Subtraction Result:", difference)       # Output: [8, 15, 20, 36]

# 3. Element-wise Multiplication (*) - The Hadamard Product
scaled_stock = inventory_store_A * inventory_store_B
print("Multiplication:    ", scaled_stock)     # Output: [20, 100, 300, 160]

# 4. Element-wise Division (/)
shares = inventory_store_A / inventory_store_B
print("Division Result:   ", shares)           # Output: [5.0, 4.0, 3.0, 10.0]

# 5. Element-wise Exponentiation (**) - Raising to a power
squared_values = inventory_store_B ** 2
print("Squared B Array:   ", squared_values)   # Output: [4, 25, 100, 16]

#2 practise
matrix_X = np.array([[2, 4], [6, 8]])
matrix_Y = np.array([[1, 2], [3, 4]])
cube_result= matrix_X ** 3
print("\nElement-wise Cubed Result:\n", cube_result)
multiplication_result = matrix_X * matrix_Y
print("\nElement-wise Multiplication Result:\n", multiplication_result)