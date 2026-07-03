import numpy as np

def calculate_contrast(img) -> int:
    min_pixel = 255
    max_pixel = 0
    for row in img:
        for pixel in row:
            if pixel < min_pixel:
                min_pixel = pixel
            if pixel > max_pixel:
                max_pixel = pixel
    return max_pixel - min_pixel

print(calculate_contrast(np.array([[0, 50], [200, 255]])))