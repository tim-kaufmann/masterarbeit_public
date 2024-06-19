# Aufgabe
Assuming there is a matrix of size=[N*N], how to set the values above its diagonal to zero, output the resulting matrix, then calculate the sum of the remaining values, and output the sum.

# Prompt
Your task is to generate python code to solve the following problem. The generated code must be placed between the ```python and ```, and only one code block is allowed: 
Assuming there is a matrix of size=[N*N], how to set the values above its diagonal to zero, output the resulting matrix, then calculate the sum of the remaining values, and output the sum.

You need to follow the function names or class names in the test cases. The generated code should not contain any test cases: 
class Testdiag_zero:
    def test_diag_zero_1(self):
        matrix = np.arange(1, 10).reshape(3, 3)
        assert diag_zero(matrix) == 34