import numpy as np

def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    return (x - np.min(x)) / (np.max(x) - np.min(x))

print(min_max([1, 2, 3, 4, 5]))