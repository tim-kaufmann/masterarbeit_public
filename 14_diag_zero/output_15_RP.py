import numpy as np

def diag_zero(matrix):
    n = matrix.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            matrix[i, j] = 0
    
    matrix_sum = np.sum(matrix)
    return matrix_sum
