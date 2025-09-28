# Considering A is of order rAxcA, and B is of order rBxcB, revise the above algorithm and
# implement it in Python. cA=rB, but rA, rB and cB can be different quantities.
from tabulate import tabulate

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

try:
    C = matmul(A, B)
except ValueError as e:
    print("Error:", e)
else:
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")
    print_matrix(C, "Matrix C (A * B)")