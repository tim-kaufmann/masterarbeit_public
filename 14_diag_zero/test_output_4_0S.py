import numpy as np
from output_4_0S import diag_zero

class Testdiag_zero:
    def test_diag_zero_2(self):
        matrix = np.arange(1, 17).reshape(4, 4)
        assert diag_zero(matrix) == 100

    def test_diag_zero_3(self):
        matrix = np.arange(1, 26).reshape(5, 5)
        assert diag_zero(matrix) == 235

    def test_diag_zero_4(self):
        matrix = np.arange(1, 37).reshape(6, 6)
        assert diag_zero(matrix) == 476

    def test_diag_zero_5(self):
        matrix = np.arange(1, 50).reshape(7, 7)
        assert diag_zero(matrix) == 868

    def test_diag_zero_6(self):
        matrix = np.arange(1, 65).reshape(8, 8)
        assert diag_zero(matrix) == 1464

    def test_diag_zero_7(self):
        matrix = np.ones((1, 1))
        assert diag_zero(matrix) == 1

    def test_diag_zero_8(self):
        matrix = np.ones((2, 2))
        assert diag_zero(matrix) == 3

    def test_diag_zero_9(self):
        matrix = np.ones((3, 3))
        assert diag_zero(matrix) == 6

    def test_diag_zero_10(self):
        matrix = np.ones((4, 4))
        assert diag_zero(matrix) == 10