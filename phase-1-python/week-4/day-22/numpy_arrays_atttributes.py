import numpy as np

# Create a 2D matrix of shape 3x4
matrix = np.ones((3, 4), dtype=np.int32)

print("Dimensions (.ndim):", matrix.ndim)
print("Layout Shape (.shape):", matrix.shape)
print("Data Type    (.dtype):", matrix.dtype)
print("Total Items  (.size): ", matrix.size)
print("RAM Weight   (.nbytes):", matrix.nbytes, "bytes")