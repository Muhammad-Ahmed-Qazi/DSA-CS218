from tabulate import tabulate

def storeTridiagonal(mat):
    n = len(mat)
    u = [0 for i in range(3 * n - 2)]
    l = 0

    for i in range(n):
        for k in range(n):
            if i == k + 1:  # Lower diagonal
                u[l] = mat[i][k]
                l += 1
            elif i == k:  # Main diagonal
                u[l] = mat[i][k]
                l += 1
            elif i == k - 1:  # Upper diagonal
                u[l] = mat[i][k]
                l += 1

    return u

def retrieveTridiagonal(u, n):
    a = [[0 for i in range(n)] for j in range(n)]
    l = 0

    for i in range(n):
        for k in range(n):
            if i == k + 1:  # Lower diagonal
                a[i][k] = u[l]
                l += 1
            elif i == k:  # Main diagonal
                a[i][k] = u[l]
                l += 1
            elif i == k - 1:  # Upper diagonal
                a[i][k] = u[l]
                l += 1

    return a

def print_matrix(M, name):
    print(f"\n{name}:")
    print(tabulate(M, tablefmt="grid"))

# Main program
A = [[5, 2, 0, 0],
     [3, 8, 4, 0],
     [0, 5, 1, 6],
     [0, 0, 7, 2]]
u = storeTridiagonal(A)
B = retrieveTridiagonal(u, 4)
print_matrix(A, "Matrix A")
print("\n1D array storing non-zero elements of A:")
print(u)
print_matrix(B, "Matrix B (retrieved from 1D array)")