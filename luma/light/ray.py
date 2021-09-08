from typing import Iterable, Tuple, List
import numpy as np

from luma.util.geometry import asCoordinate, asHomogeneous
from luma.world.world import World

class Ray():
    start: np.array
    end: np.array
    screen_pos: Tuple[int, int]
    intersections: List[Tuple[float, 'BodyEntity']]

    def __init__(
        self,
        screen_pos: Iterable,
        start: np.array,
        end: np.array,
        camera_mat: np.array
    ) -> None:
        self.screen_pos = tuple(screen_pos)
        self.start = asCoordinate(camera_mat.dot(asHomogeneous(start)))
        self.end = asCoordinate(camera_mat.dot(asHomogeneous(end)))
    
    def get_point(self, t: float) -> np.array:
        start = self.start
        end = self.end
        return start + (t * (end - start))

    def set_and_sort_intersections(self, intersections: List[Tuple[float, 'BodyEntity']]) -> None:
        self.intersections = intersections
        self.intersections.sort(
            reverse=False,
            key=lambda x: x[0]
        )

    def get_intersection_color(self, world: World) -> np.array:
        """ Get the color of associated with the ray given the
            intersections with the BodyEntities in the world.

            Assumption: set_and_sort_intersections has been called.
        """

        color = np.zeros(3)
        if len(self.intersections):
            color = self.intersections[0][1].material.i_ambient

        return color
