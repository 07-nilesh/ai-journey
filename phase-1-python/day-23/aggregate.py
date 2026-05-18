import numpy as np

# Create a 2x3 sample score grid
scores = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# 1. Complete aggregate (No axis)
print("Grand Total Sum:", np.sum(scores)) 
# Output: 210 (10+20+30+40+50+60)

# 2. Column-wise Sum (axis=0) -> Collapses downwards
print("Column-wise Sum:", np.sum(scores, axis=0))
# Output: [50, 70, 90]  -> (10+40, 20+50, 30+60)

# 3. Row-wise Mean (axis=1) -> Collapses sideways
print("Row-wise Average:", np.mean(scores, axis=1))
# Output: [20. 50.] -> (Average of row 0, Average of row 1)

#2 practise
data_matrix = np.array([
    [5,  22, 18],
    [14, 9,  31]
])
max_value = np.max(data_matrix,axis=0)
print("\nColumn-wise Max Values:", max_value)
max_value_row = np.max(data_matrix,axis=1)
print("Row-wise Max Values:", max_value_row)
index_of_max = np.argmax(data_matrix, axis=1)
print("Index of Max Values in Each Row:", index_of_max)
std_dev = np.std(data_matrix, axis=0)
print("Column-wise Standard Deviation:", std_dev)
