import numpy as np

# Create a symmetric matrix
matrix_M = np.array([
    [1, 2],
    [2, 1]
])

# Extract eigenvalues and eigenvectors simultaneously
eigenvalues, eigenvectors = np.linalg.eig(matrix_M)

print("1. Eigenvalues (Scaling factors):\n", eigenvalues)
# Output: [ 3. -1.]

print("\n2. Eigenvectors (Direction matrix, column-by-column):\n", eigenvectors)

lam = eigenvalues[0]  # First eigenvalue
print("\n3. Eigenvalue (λ):", lam)
v = eigenvectors[:, 0]  # Corresponding eigenvector (first column)
print("\n4. Corresponding Eigenvector (v):\n", v)
left_side = matrix_M @ v
print("\n5. Left-hand side (M @ v):\n", left_side)
right_side = lam * v
print("\n6. Right-hand side (λ * v):\n", right_side)
