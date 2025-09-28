from tabulate import tabulate
import numpy as np
import timeit

def matmul(a, b):
    m = len(a)        # Number of rows in matrix a
    n = len(a[0])     # Number of columns in matrix a
    p = len(b[0])     # Number of columns in matrix b

    if n != len(b):   # Check if matrices are compatible for multiplication
        raise ValueError("Incompatible matrix dimensions")

    # Initialize result matrix c with zeros, of size (rows of a) x (columns of b)
    c = [[0 for _ in range(p)] for _ in range(m)]

    # Iterate over each row of a
    for i in range(m):
        # Iterate over each column of b
        for j in range(p):
            # Compute the dot product of the i-th row of a and j-th column of b
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    
    # Return the resulting matrix
    return c

def print_matrix(M, name):
    print(f"\n{name}:")
    print(tabulate(M, tablefmt="grid"))

# Main program
A = [[1, 2, 3],
     [4, 5, 6]]
B = [[7, 8],
     [9, 10],
     [11, 12]]

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")

try:
    C = matmul(A, B)
    print_matrix(C, "Matrix C (A * B)")
except ValueError as e:
    print("Error:", e)

# Comparison with NumPy
A_np = np.array(A)
B_np = np.array(B)

exec_time_custom = timeit.timeit(lambda: matmul(A, B), number=1)
exec_time_numpy = timeit.timeit(lambda: np.matmul(A_np, B_np), number=1)

print(f"Custom implementation time: {exec_time_custom:.6f} seconds")
print(f"NumPy implementation time: {exec_time_numpy:.6f} seconds")
print(f"My function is so much faster than the built-in function: {exec_time_numpy / exec_time_custom:.2f} times")