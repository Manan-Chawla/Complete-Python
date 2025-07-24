import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

for a1,b1 in A,B:
 print(a1+b1)      # [[ 6  8] [10 12]]
print(A @ B)      # Matrix multiplication
print(A.T)        # Transpose
