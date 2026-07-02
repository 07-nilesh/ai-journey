import numpy as np

# 1. np.linalg.norm (The Measuring Tape)
vec = np.array([3, 4]) 
# Math check: sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5
print("Vector Magnitude (Norm):", np.linalg.norm(vec)) # Output: 5.0


# 2. np.linalg.det & np.linalg.inv (The Matrix Tools)
matrix_A = np.array([
    [1, 2],
    [3, 4]
])

# Calculate the scaling factor of this space
determinant = np.linalg.det(matrix_A)
print("\nDeterminant of A:", determinant) # Output is roughly -2.0

# Generate the "Undo" Inverse Matrix
matrix_A_inv = np.linalg.inv(matrix_A)
print("\nInverse Matrix of A:\n", matrix_A_inv)

# Prove that A multiplied by its Inverse yields the Identity Matrix (I)
identity_test = matrix_A @ matrix_A_inv
print("\nMultiplication Proof (A @ A_inv):\n", np.round(identity_test))

#2 Practice
bad_matrix = np.array([
    [1, 2],
    [2, 4]
])
print("\nDeterminant of Bad Matrix:", np.linalg.det(bad_matrix)) # Output should be 0, indicating it's singular
try:
    bad_matrix_inv = np.linalg.inv(bad_matrix)
    print("\nInverse of Bad Matrix:\n", bad_matrix_inv)
except np.linalg.LinAlgError:
    print("\nBad Matrix is singular and cannot be inverted.")
