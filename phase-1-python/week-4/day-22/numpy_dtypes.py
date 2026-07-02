import numpy as np

# Create an array of 1 million integers using default int64
large_int64_array = np.arange(1000000)

# Create the exact same array, but explicitly force it to use int32
large_int32_array = np.arange(1000000, dtype=np.int32)

# Check the memory consumption
bytes_64 = large_int64_array.nbytes
bytes_32 = large_int32_array.nbytes

print(f"int64 Array Size: {bytes_64} bytes (~{bytes_64 / 10**6:.2f} MB)")
print(f"int32 Array Size: {bytes_32} bytes (~{bytes_32 / 10**6:.2f} MB)")
print(f"Memory Saved: {((bytes_64 - bytes_32) / bytes_64) * 100}%")

# Let's see the defaults for floats
default_float = np.array([1.5, 2.5, 3.5])
forced_float32 = np.array([1.5, 2.5, 3.5], dtype=np.float32)

print("\nDefault Float Dtype:", default_float.dtype)
print("Forced Float32 Dtype:", forced_float32.dtype)

#2
D_array=np.ones((5000,5000))
print(D_array.dtype)
print(D_array.nbytes/10**6,"MB")
matrix=D_array.astype(np.float32)
print(matrix.dtype)
print(matrix.nbytes/10**6,"MB")
print(f"Memory Saved: {((D_array.nbytes - matrix.nbytes) / D_array.nbytes) * 100:.2f}%")