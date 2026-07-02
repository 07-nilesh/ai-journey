import numpy as np

# Create a 3x3 grid matrix
grid = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 1. Broadcasting a single Scalar (Shape 1,) across a 2D Matrix (Shape 3,3)
print("Scalar Broadcast:\n", grid + 2) 
# Notice: 2 was added to every single position!

# 2. Broadcasting a 1D Vector (Shape 3,) across a 2D Matrix (Shape 3,3)
row_vector = np.array([1, 2, 3]) # Represents additions for Col 0, Col 1, Col 2
broadcast_result = grid + row_vector

print("\nVector Broadcast:\n", broadcast_result)
# Row 1 becomes: [10+1, 20+2, 30+3] -> [11, 22, 33]
# Row 2 becomes: [40+1, 50+2, 60+3] -> [41, 52, 63]

#2 practise
matrix_M = np.ones((4, 3))  # 4 rows, 3 columns
vector_V = np.array([10, 20, 30,40])
try: # 4 elements (Shape: 4,)
    print("\nPractise Result:\n", matrix_M + vector_V)
except ValueError as e:
    print("\nError during broadcasting:", e)
# Reshape vector_V from (4,) to (4, 1) to make it a vertical column
vector_column = vector_V.reshape(4, 1)

print("New Vector Shape:", vector_column.shape)
print("\nSuccessful Broadcast Result:\n", matrix_M + vector_column)