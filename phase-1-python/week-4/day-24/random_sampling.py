import numpy as np

# --- 1. Random Generators ---
uniform_decimals = np.random.rand(2, 3)    # Uniform distribution [0, 1)
print("Uniform Decimals:\n", uniform_decimals)
normal_decimals  = np.random.randn(2, 3)   # Standard Normal distribution (Mean=0, SD=1)
print("Normal Decimals:\n", normal_decimals)
random_integers  = np.random.randint(1, 10, size=(2, 3)) # Whole numbers from 1 to 9
print("Random Integers:\n", random_integers)

#--- 2. Stacking Arrays ---
block_1 = np.array([[1, 2, 3], [4, 5, 6]])
block_2 = np.array([[7, 8, 9], [10, 11, 12]])

# Stack vertically (Top-to-Bottom) -> Output shape changes to (4, 3)
vertical_combo = np.vstack((block_1, block_2))
print("Vertical Stack:\n", vertical_combo)

# Stack horizontally (Side-by-Side) -> Output shape changes to (2, 6)
horizontal_combo = np.hstack((block_1, block_2))
print("\nHorizontal Stack:\n", horizontal_combo)

# --- 3. Splitting Arrays ---
# Let's take our 4-row vertical_combo and cut it back in half vertically
top_half, bottom_half = np.vsplit(vertical_combo, 2)
print("\nSplit Top Half:\n", top_half)
print("\nSplit Bottom Half:\n", bottom_half)
left_half, right_half = np.hsplit(horizontal_combo, 2)
print("\nSplit Left Half:\n", left_half)
print("\nSplit Right Half:\n", right_half)

#2 practise
features_A=np.random.randn(3,2)
features_B=np.random.rand(3,3)
try:
    vertical_combination=np.vstack((features_A,features_B))
    print("\nVertical Combination:\n", vertical_combination)
    horizontal_combination=np.hstack((features_A,features_B))
    print("\nHorizontal Combination:\n", horizontal_combination)
except ValueError as e:
    print("Error:", e)

# Create two simple 1D vectors of shape (3,)
array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

# --- 1. Concatenate (Glue together along an existing axis) ---
concat_result = np.concatenate((array_1, array_2), axis=0)
print("Concatenate Result: ", concat_result)
# Output: [1 2 3 4 5 6]
print("Concatenate Shape:  ", concat_result.shape) 
# Output: (6,) -> Still a 1D vector, just longer!


# --- 2. Stack (Pile together to build a completely NEW axis) ---
stack_result = np.stack((array_1, array_2), axis=0)
print("\nStack Result:\n", stack_result)
# Output: 
# [[1 2 3]
#  [4 5 6]]
print("Stack Shape:         ", stack_result.shape) 
# Output: (2, 3) -> Upcasted to a 2D matrix!