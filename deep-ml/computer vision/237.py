import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    image = np.array(image, dtype=float)

    if image.size == 0 or image.ndim != 3 or image.shape[2] != 3:
        return -1

    if np.any((image < 0) | (image > 255)):
        return -1

    gray_coef = [0.299, 0.587, 0.114]
    result = []

    for row in image:
        gray_row = []
        for pixel in row:
            r, g, b = pixel
            gray_value = r * gray_coef[0] + g * gray_coef[1] + b * gray_coef[2]
            gray_row.append(int(round(gray_value)))
        result.append(gray_row)
    return result

image = [[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [255, 255, 255]]]
print(rgb_to_grayscale(image))