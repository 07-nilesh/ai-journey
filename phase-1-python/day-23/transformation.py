import numpy as np

# Create a flat 1D line of 12 elements
flat_line = np.arange(12) # [0, 1, 2, ... 11]

# 1. Reshape into a 3x4 grid matrix
matrix_3x4 = flat_line.reshape(3, 4)
print("Reshaped Grid (3x4):\n", matrix_3x4)

# 2. Transpose it (Flip rows and columns)
# Original shape was (3,4) -> New shape will be (4,3)
transposed_matrix = matrix_3x4.T
print("\nTransposed Grid (4x3):\n", transposed_matrix)

# 3. Flatten vs Ravel
# Let's squash our 3x4 matrix back to 1D using ravel
#raveled_view = matrix_3x4.ravel()
#raveled_view[0] = 999  # Change the very first element in the view!
flatten_view = matrix_3x4.flatten()
flatten_view[0] = 999  # Change the very first element in the flattened copy

print("\nModified view element to 999...")
print("Original Matrix row 0, col 0 is now:", matrix_3x4[0, 0])
# Look at that! The original matrix changed because ravel shares memory! while flatten does not affect the original matrix.


#2 practise
sample_vector = np.arange(20) # 20 elements total
reshaped=sample_vector.reshape(5,-1) # Reshape to 5 rows and automatically determine columns
print("\nReshaped Sample Vector (5 rows):\n", reshaped)
print(reshaped.shape) # Output: (5, 4) -> 5 rows, 4 columns