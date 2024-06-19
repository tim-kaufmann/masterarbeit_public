import numpy as np

def diag_zero(matrix):
    # Set the values above the diagonal to zero
    N = matrix.shape[0]
    for i in range(N):
        for j in range(i + 1, N):
            matrix[i, j] = 0
    
    # Calculate the sum of the remaining values
    matrix_sum = np.sum(matrix)
    
    return matrix_sum