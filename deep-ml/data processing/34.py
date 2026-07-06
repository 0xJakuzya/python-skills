import numpy as np

def to_categorical(x, n_col=None):
	return np.eye(np.max(x) + 1)[x]

x = np.array([0, 1, 2, 1, 0])
print(to_categorical(x))