import numpy as np

def diag_zero(matrix):
    # Set the values above the diagonal to zero
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j] = 0
    
    # Output the resulting matrix
    print("Resulting Matrix:")
    print(matrix)
    
    # Calculate the sum of the remaining values
    total_sum = np.sum(matrix)
    
    # Output the sum
    print("Sum of remaining values:", total_sum)
    
    return total_sum
