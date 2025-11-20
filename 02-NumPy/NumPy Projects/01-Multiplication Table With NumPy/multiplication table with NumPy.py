# Simulating a multiplication table with NumPy
# Goal: Build a multiplication table from 1 to 10 using broadcasting

import numpy as np  # Import the NumPy library for numerical operations

x = np.arange(1, 11)  # Create a 1D array with values from 1 to 10

# Reshape x into a column vector using [:, None] and multiply by x (row vector)
# This uses broadcasting to generate a 10x10 multiplication table
table = x[:, None] * x

print("Multiplication Table from 1 to 10:")
print(table)  # Display the resulting table
