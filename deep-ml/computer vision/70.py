def calculate_brightness(img):
    total = 0
    count = 0

    if len(img) == 0:
        return -1 

    row_len = len(img[0])

    if row_len == 0:
        return -1

    for row in img:
        if len(row) != row_len:
            return -1

        for pixel in row:
            if pixel < 0 or pixel > 255:
                return -1
            total += pixel
            count += 1
            
    return total / count  

print(calculate_brightness([]))