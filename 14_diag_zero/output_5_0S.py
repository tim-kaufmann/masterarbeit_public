import numpy as np

def diag_zero(matrix):
    n = matrix.shape[0]
    # Set values above the diagonal to zero
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i, j] = 0
    
    # Calculate the sum of the remaining values
    total_sum = np.sum(matrix)
    
    # Output the resulting matrix and the sum
    print(matrix)
    print(total_sum)
    
    return total_sum
