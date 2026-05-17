import numpy as np
basic_vector=np.array([5,10,15,20])
print(type(basic_vector))

# Create a numpy array with an integer and a float
mixed_array = np.array([1, 2.5, 3])
print("Array content:", mixed_array)
print("Array data type:", mixed_array.dtype)

# 1. Creating a blank 2D canvas of zeros (Rows, Columns)
# Note the double parentheses because shape is passed as a tuple
blank_scores = np.zeros((3, 5))
print("Zeros Matrix:\n", blank_scores)

# 2. Creating a baseline array of ones
baseline_multipliers = np.ones((2, 4))
print("\nOnes Matrix:\n", baseline_multipliers)

# 3. Generating sequences with np.arange(start, stop, step)
# Let's generate odd numbers between 1 and 10
odd_sequence = np.arange(1, 10, 2)
print("\nSequence (1 to 10, step 2):", odd_sequence)
# Output: [1, 3, 5, 7, 9] (Notice 10 is excluded)

blank_matrix = np.zeros((4, 3))
blank_array=np.ones((2,2))
print(blank_array+5)
multipleoften=np.arange(0, 101, 10)
print(multipleoften)

# Generate a 1D array of 5 random bell-curve numbers
vector_samples = np.random.randn(5)
print("1D Random Samples:\n", vector_samples)

# Generate a 2D matrix of shape 3 rows and 4 columns
weight_matrix = np.random.randn(3, 4)
print("\n2D Weight Matrix:\n", weight_matrix)

# Create a 3x3 diagonal anchor grid
identity_grid = np.eye(3) 
print("\nIdentity Matrix:\n", identity_grid)

# Generate exactly 5 numbers evenly spaced between 0 and 10
snapped_intervals = np.linspace(0, 10, 5) 
print("\nEvenly Spaced Intervals:\n", snapped_intervals)
# Output will be: [0. , 2.5, 5. , 7.5, 10.]