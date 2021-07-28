from typing import Iterable
import numpy as np

from luma.world.entity.entity import Entity

class Camera(Entity):
    name: str
    point: Iterable
    direction: Iterable
    focal_length: float

    def __init__(
        self,
        name: str,
        point: Iterable,
        direction: Iterable,
        focal_length: float,
        window_width: int,
        window_height: int,
        screen_width: float,
        screen_height: float,
    ):
        self.name = name
        self.point = point
        self.direction = np.array(direction) / np.linalg.norm(direction)
        self.focal_length = focal_length
        self.window_width = window_width
        self.window_height = window_height
        self.screen_width = screen_width
        self.screen_height = screen_height
