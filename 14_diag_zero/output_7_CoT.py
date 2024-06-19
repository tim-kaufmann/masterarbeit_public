import numpy as np

def diag_zero(matrix):
    # Get the number of rows (and columns) in the square matrix
    N = matrix.shape[0]
    
    # Set the values above the diagonal to zero
    for i in range(N):
        for j in range(i + 1, N):
            matrix[i, j] = 0
    
    # Output the resulting matrix (for debugging purposes)
    print(matrix)
    
    # Calculate the sum of the remaining values
    total_sum = np.sum(matrix)
    
    # Output the sum
    return total_sum
