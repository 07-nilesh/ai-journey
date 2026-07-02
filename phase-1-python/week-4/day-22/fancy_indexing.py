import numpy as np

# --- 1D Fancy Indexing ---
items = np.array(["Apples", "Bananas", "Cherries", "Dates", "Elderberries"])

# Pass a list of the exact indices you want to grab
custom_grab = items[[0, 1, 4]]
print("1D Selected Items:", custom_grab)
# Output: ['Apples' 'Bananas' 'Elderberries']


# --- 2D Fancy Indexing (Selecting Specific Rows) ---
matrix = np.array([
    [10, 20],  # Row 0
    [30, 40],  # Row 1
    [50, 60],  # Row 2
    [70, 80]   # Row 3
])

# Let's extract Row 3 and Row 0, in that exact order!

selected_rows = matrix[[3, 0]]
print("\n2D Selected Rows:\n", selected_rows)
# Output:
# [[70, 80],
#  [10, 20]]

#2 practise
alpha_array = np.array([100, 200, 300, 400, 500, 600, 700])
selected_elements = alpha_array[[4, 1, -1]]
print("\nSelected Elements:", selected_elements)