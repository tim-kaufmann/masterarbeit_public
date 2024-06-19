import numpy as np

def diag_zero(matrix):
    N = matrix.shape[0]
    for i in range(N):
        for j in range(i + 1, N):
            matrix[i, j] = 0
    result_sum = np.sum(matrix)
    print(matrix)
    print(result_sum)
    return result_sum
