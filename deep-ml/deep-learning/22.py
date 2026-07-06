import math
import numpy as np

def sigmoid(z: float) -> float:
    return 1 / (1 + np.exp(-z))

z = 0
print(sigmoid(z)) # 0.5