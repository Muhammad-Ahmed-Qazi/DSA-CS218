def storeTriangular(a):
    u = list()
    i = 0
    for j in range(len(a)):
        for k in range(j + 1):
            u.append(a[j][k])
            i += 1
    return u

def retrieveTriangular(u):
    a = list()
    for j in range(len(u)):
        for k in range(len(u)):
            if k > j:
                a[j][k] = 0
            else:
                a[j][k] = u[int(0.5 * j * (j + 1) + k)]
    return a

# Main Program
A = [[1, 0, 0, 0],
     [2, 3, 0, 0],
     [4, 5, 6, 0],
     [7, 8, 9, 10]]
U = storeTriangular(A)
print("The stored array is:", U)
B = retrieveTriangular(U)
print("The retrieved array is:", B)