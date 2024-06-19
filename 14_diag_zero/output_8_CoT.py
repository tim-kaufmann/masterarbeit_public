import numpy as np

def diag_zero(matrix):
    # Get the size of the matrix
    N = matrix.shape[0]
    
    # Create a mask for the upper triangle above the diagonal
    mask = np.triu(np.ones((N, N)), k=1)
    
    # Set values above the diagonal to zero
    matrix[mask == 1] = 0
    
    # Calculate the sum of the remaining values
    total_sum = np.sum(matrix)
    
    # Output the resulting matrix and the sum
    print(matrix)
    print(total_sum)
    
    return total_sum
