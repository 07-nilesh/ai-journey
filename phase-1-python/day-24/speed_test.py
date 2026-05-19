import numpy as np
import time

# 1. Initialize two 100x100 matrices with random floats
SIZE = 100
A = np.random.randn(SIZE, SIZE)
B = np.random.randn(SIZE, SIZE)

# Initialize an empty matrix of zeros to hold our manual loop results
result_manual = np.zeros((SIZE, SIZE))


# --- METHOD 1: Manual Matrix Multiplication using Triple Loops ---
start_time = time.time()

for i in range(SIZE):          # Loop through rows of A
    for j in range(SIZE):      # Loop through columns of B
        for k in range(SIZE):  # Loop through matching inner dimensions
            result_manual[i, j] += A[i, k] * B[k, j]

end_time = time.time()
manual_duration = end_time - start_time
print(f"1. Manual Loop Time: {manual_duration:.6f} seconds")


# --- METHOD 2: Optimized NumPy Vectorized Multiplication ---
start_time = time.time()

result_numpy = A @ B

end_time = time.time()
numpy_duration = end_time - start_time
print(f"2. NumPy '@' Time:   {numpy_duration:.6f} seconds")


# --- VERIFICATION: Ensure the math matches perfectly ---
assert np.allclose(result_manual, result_numpy), "Math mismatch occurred!"
print("\nMath verification passed successfully! Both matrices match.")

# --- THE SPEEDUP FACTOR ---
try:
    speedup = manual_duration / numpy_duration
    print(f"\n🚀 NumPy was approximately {speedup:.1f}x FASTER than your loops!")
except ZeroDivisionError:
    print("\n🚀 NumPy was significantly faster than your loops!")