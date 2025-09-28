# SciPy. (pronounced "Sigh Pie") is a free and open-source Python library used for scientific
# computing and technical computing. SciPy provides tools for creating sparse matrices using
# multiple data structures, as well as tools for converting a dense matrix to a sparse matrix.
# Write a program to define a 3 x 6 sparse matrix as a dense array, convert it to a CSR
# (Compressed sparse row) sparse representation, and then convert it back to a dense array.
import scipy
import numpy as np

# Define a 3x6 sparse matrix as a dense array
dense_matrix = np.array([[0, 0, 3, 0, 4, 0],
                         [0, 0, 5, 7, 0, 0],
                         [0, 2, 6, 0, 0, 0]])
print("Dense Matrix:")
print(dense_matrix)

# Convert the dense matrix to a CSR sparse representation
sparse_matrix = scipy.sparse.csr_matrix(dense_matrix)
print("\nCSR Sparse Matrix:")
print(sparse_matrix)

# Convert the CSR sparse matrix back to a dense array
converted_dense_matrix = sparse_matrix.toarray()
print("\nConverted Back to Dense Matrix:")
print(converted_dense_matrix)
