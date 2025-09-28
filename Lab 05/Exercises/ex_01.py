# Sparse matrices: stored in 1D arrays, as zero values are not stored. (triangular matrix, tridiagonal matrix)
from tabulate import tabulate

def storeTriangular(mat):
    u = [0 for i in range(int(0.5 * len(mat) * (len(mat) + 1)))]
    i = 0

    for j in range(len(mat)):
        for k in range(j + 1):
            u[i] = mat[j][k]
            i += 1

    return u

def retrieveTriangular(u, n):
    a = [[0 for i in range(n)] for j in range(n)]
    
    for j in range(n):
        for k in range(j + 1):
            a[j][k] = u[int(0.5 * j * (j + 1)) + k]   

    return a

def print_matrix(M, name):
    print(f"\n{name}:")
    print(tabulate(M, tablefmt="grid"))

# Main program
A = [[1, 0, 0],
     [2, 3, 0],
     [4, 5, 6]]
u = storeTriangular(A)
B = retrieveTriangular(u, 3)
print_matrix(A, "Matrix A")
print("\n1D array storing non-zero elements of A:")
print(u)
print_matrix(B, "Matrix B (retrieved from 1D array)")
