#1 1D Array slicing
import numpy as np
arr_1d = np.array([10, 20, 30, 40, 50, 60])

# Grab index 1 up to (but excluding) index 4
print(arr_1d[1:4]) 
# Output: [20, 30, 40]

# Grab everything from index 3 to the end
print(arr_1d[3:])   
# Output: [40, 50, 60]

#2 2D Array slicing
# Create a 3x4 grid matrix
matrix_2d = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

# Pattern A: Get a specific row
print(matrix_2d[1, :])     
# Output: [5, 6, 7, 8] (Row index 1, all columns)

# Pattern B: Get a specific column (Crucial for splitting features in ML!)
print(matrix_2d[:, 2])     
# Output: [3, 7, 11] (All rows, Column index 2)

# Pattern C: Get a sub-grid block (Top-left 2x2 corner)
print(matrix_2d[0:2, 0:2]) 
# Output: 
# [[1, 2],
#  [5, 6]]

#3 3D Array slicing
# Create a 3D array: 2 distinct matrices, each sized 2x3
cube_3d = np.array([
    [[1, 2, 3],     # Matrix 0
     [4, 5, 6]],
    
    [[7, 8, 9],     # Matrix 1
     [10, 11, 12]]
])

# Pattern A: Extract the entire first matrix layer
print(cube_3d[0, :, :]) 
# Output:
# [[1, 2, 3],
#  [4, 5, 6]]

# Pattern B: Extract the first row from EVERY matrix layer
print(cube_3d[:, 0, :])
# Output:
# [[1, 2, 3],  (from matrix 0)
#  [7, 8, 9]]  (from matrix 1)

# Practise
practice_grid = np.array([
    [10, 11, 12, 13],
    [14, 15, 16, 17],
    [18, 19, 20, 21]
])
print(practice_grid[:,3])  
print(practice_grid[1:3,1:3])