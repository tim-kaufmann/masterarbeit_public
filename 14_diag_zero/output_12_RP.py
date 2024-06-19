import numpy as np

def diag_zero(matrix):
    N = matrix.shape[0]
    for i in range(N):
        for j in range(i + 1, N):
            matrix[i][j] = 0
    matrix_sum = np.sum(matrix)
    return matrix_sum

# Example usage:
# matrix = np.arange(1, 10).reshape(3, 3)
# print(diag_zero(matrix))  # Output should be 34
