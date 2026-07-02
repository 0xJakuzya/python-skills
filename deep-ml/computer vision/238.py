def flip_image(image, direction):
    if len(image) == 0:
        return -1

    if direction not in ['horizontal', 'vertical']:
        return -1

    if direction == 'horizontal':
        return [row[::-1] for row in image]

    if direction == 'vertical':
        return image[::-1]
    

image2d = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9,], [10, 11, 12]]
]
image3d = [[[255, 0, 0], [0, 255, 0], [0, 0, 255]]]
direction = 'horizontal'

print(flip_image(image3d, direction)) 
print(flip_image(image2d, direction))    