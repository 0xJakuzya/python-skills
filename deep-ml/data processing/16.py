import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    return (data - np.mean(data, axis=0)) / (np.std(data, axis=0)), (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))

data = np.array([[1, 2], [3, 4], [5, 6]])
print(feature_scaling(data))