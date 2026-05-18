import numpy as np

# Matrix X shape: (2, 3) - 2 rows, 3 columns
matrix_X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Matrix Y shape: (3, 2) - 3 rows, 2 columns
# (Inner dimensions match: 3 == 3!)
matrix_Y = np.array([
    [7,  8],
    [9,  10],
    [11, 12]
])

# Method 1: The modern '@' operator (Highly Recommended)
result_operator = matrix_X @ matrix_Y

# Method 2: np.matmul()
result_matmul = np.matmul(matrix_X, matrix_Y)

# Method 3: np.dot()
result_dot = np.dot(matrix_X, matrix_Y)

print("Matrix Multiplication Result:\n", result_matmul)
print("\nOutput Shape:", result_operator.shape) # Output shape will be (2, 2)

#2 practise
A = np.array([[1, 2], [3, 4]]) # Shape (2, 2)
B = np.array([10, 20, 30])     # Shape (3,)
# This will raise an error because the inner dimensions do not match (2 != 3)
try:
    result_practise = A @ B
except ValueError as e:
    print("\nError during matrix multiplication:", e)
