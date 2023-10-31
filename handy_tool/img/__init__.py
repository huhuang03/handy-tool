import random

import cv2
import numpy as np

def gen_random_color():
    return random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)

def main():
    """
    this gen a random image
    """
    has_alpha = False
    width = 100
    height = 100

    if has_alpha:
        img = np.full((width, height, 4), (0, 0, 0, 255))
    else:
        img = np.full((width, height, 3), (0, 0, 0))
    for r in range(0, img.shape[0]):
        for c in range(0, img.shape[1]):
            if has_alpha:
                color = gen_random_color() + (255, )
            else:
                color = gen_random_color()
            img[r, c] = color
    cv2.imwrite('random_img.png', img)

