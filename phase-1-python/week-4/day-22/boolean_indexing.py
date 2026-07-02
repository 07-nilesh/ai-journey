import numpy as np

arr = np.array([2, 8, 3, 11, 4, 14])

# Step 1: Generate the boolean mask
mask = arr > 5
print("1. The Mask Array:", mask)
# Output: [False  True False  True False  True]

# Step 2: Feed the mask back into the brackets
result = arr[mask]
print("2. Filtered Output:", result)
# Output: [ 8 11 14]

#2 practise
num_grid = np.array([
    [10, 15, 20],
    [25, 30, 35]
])
mask = num_grid % 2 != 0
print("Boolean Mask:\n", mask)
print("Filtered Output:\n", num_grid[mask])