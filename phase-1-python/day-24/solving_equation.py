import numpy as np

# 1. Map out the left-hand side coefficients matrix (A)
matrix_A = np.array([
    [1, 1, 1],
    [0, 2, 5],
    [2, 5, -1]
])

# 2. Map out the right-hand side constants vector (b)
vector_b = np.array([6, -4, 27])

# 3. Solve for the unknown variables [x, y, z] using np.linalg.solve
unknowns = np.linalg.solve(matrix_A, vector_b)

print("Values of [x, y, z]:", unknowns)

# 4. Verification Check: Matrix multiplication should yield vector_b
print("Verification (A @ unknowns):", matrix_A @ unknowns)