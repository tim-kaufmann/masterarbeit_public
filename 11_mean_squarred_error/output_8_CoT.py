import numpy as np

def mean_squared_error(y_true, y_pred):
    squared_diff = (y_true - y_pred) ** 2
    mse = np.mean(squared_diff)
    return mse
