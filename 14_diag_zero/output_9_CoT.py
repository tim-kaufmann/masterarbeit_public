import numpy as np

def diag_zero(matrix):
    n = matrix.shape[0]  # Assuming matrix is a square matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i, j] = 0
    print(matrix)
    return np.sum(matrix)
