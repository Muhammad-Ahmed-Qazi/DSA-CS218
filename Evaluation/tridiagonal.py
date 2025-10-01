# Tridiagonal matrix: 1) storage into 1D list 2) retrieval from 1D list into 2D matrix
def storage(matrix):
    tridiagonal = list() 
    pos = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if j == (i - 1) and i != (0):
                tridiagonal.append(matrix[i][j])
                pos += 1
            if j == i:
                tridiagonal.append(matrix[i][j])
                pos += 1
            if j == (i + 1) and i != (len(matrix) - 1):
                tridiagonal.append(matrix[i][j])
                pos += 1
    
    return tridiagonal

def retrieve(tridiagonal, n):
    matrix = [[0 for i in range(n)] for i in range(n)]
    pos = 0

    for i in range(n):
        for j in range(n):
            if j == (i - 1) and i != 0:
                matrix[i][j] = tridiagonal[pos]; pos += 1
            if j == i:
                matrix[i][j] = tridiagonal[pos]; pos += 1
            if j == (i + 1) and i != (n - 1):
                matrix[i][j] = tridiagonal[pos]; pos += 1
        
    return matrix

# Main program
matrix = [[1, 6, 0, 0, 0],
          [7, 2, 8, 0, 0],
          [0, 9, 3, 10, 0],
          [0, 0, 11, 4, 12],
          [0, 0, 0, 13, 5]]

tridiagonal = storage(matrix)
print(tridiagonal)
print(retrieve(tridiagonal, int((len(tridiagonal) + 2) / 3)))