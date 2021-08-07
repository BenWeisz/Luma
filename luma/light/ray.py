import numpy as np

from luma.util.geometry import asCoordinate, asHomogeneous

class Ray():
    start: np.array
    end: np.array

    def __init__(
        self,
        start: np.array,
        end: np.array,
        camera_mat: np.array
    ) -> None:
        self.start = asCoordinate(camera_mat.dot(asHomogeneous(start)))
        self.end = asCoordinate(camera_mat.dot(asHomogeneous(end)))
    
    def get_point(self, t: float) -> np.array:
        start = self.start
        end = self.end
        return start + (t * (end - start))
