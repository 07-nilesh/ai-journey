import sys
import numpy as np

print("\n--- CONDA ENVIRONMENT TEST ---")

# 1. Check the Python engine
print(f"Python Version: {sys.version.split()[0]}") 

# 2. Check the Numpy library
print(f"Numpy Version: {np.__version__}")

# 3. Prove the C++ math backend is working
my_array = np.array([10, 20, 30])
result = my_array * 5
print(f"Numpy Math Test (array * 5): {result}")

print("------------------------------")
print("If you see this without errors, your steel box is PERFECT! 🎉\n")