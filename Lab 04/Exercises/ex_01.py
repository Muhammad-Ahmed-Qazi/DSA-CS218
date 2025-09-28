from tabulate import tabulate

def matmul(a, b):
    n = len(a)
    c = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def print_matrix(M, name):
    print(f"\n{name}:")
    print(tabulate(M, tablefmt="grid"))

# Main program
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

C = matmul(A, B)

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")
print_matrix(C, "Matrix C (A * B)")