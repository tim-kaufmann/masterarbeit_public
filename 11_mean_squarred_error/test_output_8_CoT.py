import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from output_8_CoT import mean_squared_error

class Testmean_squared_error:
    def test_mean_squared_error_2(self):
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([2, 3, 4, 5, 6])
        assert mean_squared_error(y_true, y_pred) == 1.0

    def test_mean_squared_error_3(self):
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([5, 4, 3, 2, 1])
        assert mean_squared_error(y_true, y_pred) == 8.0

    def test_mean_squared_error_4(self):
        y_true = np.array([1, 1, 1, 1, 1])
        y_pred = np.array([1, 1, 1, 1, 1])
        assert mean_squared_error(y_true, y_pred) == 0.0

    def test_mean_squared_error_5(self):
        y_true = np.array([1, 1, 1, 1, 1])
        y_pred = np.array([0, 0, 0, 0, 0])
        assert mean_squared_error(y_true, y_pred) == 1.0

    def test_mean_squared_error_6(self):
        y_true = np.array([0, 0, 0, 0, 0])
        y_pred = np.array([1, 1, 1, 1, 1])
        assert mean_squared_error(y_true, y_pred) == 1.0

    def test_mean_squared_error_7(self):
        y_true = np.array([100, 200, 300, 400, 500])
        y_pred = np.array([100, 200, 300, 400, 500])
        assert mean_squared_error(y_true, y_pred) == 0.0

    def test_mean_squared_error_8(self):
        y_true = np.array([100, 200, 300, 400, 500])
        y_pred = np.array([500, 400, 300, 200, 100])
        assert mean_squared_error(y_true, y_pred) == 80000.0

    def test_mean_squared_error_9(self):
        y_true = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
        y_pred = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
        assert mean_squared_error(y_true, y_pred) == 0.0