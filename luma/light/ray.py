from typing import Tuple, Interable
import numpy as np

from luma.util.geometry import asCoordinate, asHomogeneous

class Ray():
    start: np.array
    end: np.array
    screen_pos: Tuple[int, int]

    def __init__(
        self,
        screen_pos: Interable[int, int],
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
