import numpy as np
from typing import Tuple

class Image():
    def __init__(self, height, width):
        self.image = np.zeros((height, width, 3))
        self.width = width
        self.height = height

    def setPixel(self, y, x, pixel: Tuple[int, int, int]) -> None:
        self.image[y, x] = np.array(pixel)

    def __getitem__(self, key):
        return self.image[key[0], key[1]]