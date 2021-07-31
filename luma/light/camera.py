from typing import Iterable
import numpy as np

from luma.world.entity.entity import Entity
from luma.light.ray import Ray

class Camera(Entity):
    name: str
    point: np.array
    xzx: np.array
    focal_length: float

    def __init__(
        self,
        name: str,
        point: Iterable,
        xzx: Iterable,
        focal_length: float,
        window_width: int,
        window_height: int,
        screen_width: float,
        screen_height: float,
    ):
        self.name = name
        self.point = np.array(point)
        self.xzx = np.array(xzx)
        self.focal_length = focal_length
        self.window_width = window_width
        self.window_height = window_height
        self.screen_width = screen_width
        self.screen_height = screen_height

    def spawnCameraSpaceRays(self) -> Iterable[Ray]:
        """ Spawn a set of camera space rays, corresponding
            to the camera parameters.

            To generate these rays we use the focal_length,
            window_width, window_height, screen_width,
            screen_height.
        """

        rays = []
        for y in range(self.window_height):
            for x in range(self.window_width):
                step_v = self.screen_height / self.window_height
                step_h = self.screen_width / self.window_width

                x_p = (step_h / 2.0) + (x * step_h) - (self.screen_width / 2.0)
                y_p = (step_v / 2.0) + (y * step_v) - (self.screen_height / 2.0)

                ray = Ray(
                    np.array([0, 0, 0]),
                    np.array([x_p, y_p, self.focal_length])
                )

                rays.append(ray)

        return rays

    @property
    def cameraMatrix(self):
        """ Generate the camera matrix corresponding
            to the camera parameters.
        """

        pass

        
