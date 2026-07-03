import numpy as np

def zero_pad_image(image, pad_width):
    """
    Add zero padding around a grayscale image.
    
    Args:
        img: 2D list or numpy array of pixel values
        pad_width: integer number of pixels to pad on each side
    
    Returns:
        Padded image as 2D list with integer values,
        or -1 if input is invalid
    """
    image = np.array(image)

    if image.size == 0 or pad_width < 0 or image.ndim != 2:
        return -1 

    return np.pad(array=image, pad_width=pad_width).tolist()

image = [
    [1, 2], 
    [3, 4]
]
print(zero_pad_image(image, 1))