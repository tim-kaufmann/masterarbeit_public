import numpy as np

def diag_zero(matrix):
    # Set the values above the diagonal to zero
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j] = 0

    # Calculate the sum of the remaining values
    remaining_sum = np.sum(matrix)
    
    return remaining_sum
