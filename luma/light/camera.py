from typing import Iterable, List
import numpy as np

from luma.world.entity.entity import Entity
from luma.light.ray import Ray
from luma.util.geometry import getRotationMatrix
from luma.world.world import World
from luma.image.image import Image

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
        self.window_width = int(window_width)
        self.window_height = int(window_height)
        self.screen_width = float(screen_width)
        self.screen_height = float(screen_height)

    def spawnCameraSpaceRays(self) -> Iterable[Ray]:
        """ Spawn a set of camera space rays, corresponding
            to the camera parameters.

            To generate these rays we use the focal_length,
            window_width, window_height, screen_width,
            screen_height.
        """

        camera_mat = self.camera_matrix
        rays = []
        for y in range(self.window_height):
            for x in range(self.window_width):
                step_v = self.screen_height / self.window_height
                step_h = self.screen_width / self.window_width

                x_p = (step_h / 2.0) + (x * step_h) - (self.screen_width / 2.0)
                y_p = (step_v / 2.0) + (y * step_v) - (self.screen_height / 2.0)

                ray = Ray(
                    screen_pos=(x, y),
                    start=np.array([0, 0, -self.focal_length]),
                    end=np.array([x_p, y_p, 0]),
                    camera_mat=camera_mat
                )

                rays.append(ray)

        return rays

    def render_frame(self, world: World) -> Image:
        """ Intersect each ray with all world objects. Compare
            all intersections and set the corresponding pixel
            to the closest intersection material.
        """

        frame = np.zeros((int(self.window_width), int(self.window_height), 3))
        frame = Image(
            height=self.window_height,
            width=self.window_width
        )

        rays_to_process = self.spawnCameraSpaceRays()
        for ray in rays_to_process:
            intersections = []
            for ent in world.body_entities:
                ent_ray_intersections = ent.intersect(ray)
                ent_ray_intersections = map(lambda t: (t, ent), ent_ray_intersections)
                intersections.extend(list(ent_ray_intersections))

            ray.set_and_sort_intersections(intersections)
            color = ray.get_intersection_color(world)

            screen_pos = ray.screen_pos
            frame.setPixel(screen_pos[1], screen_pos[0], color)

        return frame

    @property
    def camera_matrix(self):
        """ Generate the camera matrix corresponding
            to the camera parameters.

            The camera matrix is a 4D affine matrix that
            transforms homogeneous coordinates in camera
            space to world space.
        """

        rotation_mat = getRotationMatrix(self.xzx)
        camera_mat = np.eye(4)
        camera_mat[:3, :3] = rotation_mat
        camera_mat[:3, 3:] = self.point.reshape((3, 1))
        return camera_mat
