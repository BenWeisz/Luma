import numpy as np

class Ray():
    start: np.array
    end: np.array
    camera_mat: np.array

    def __init__(
        self,
        start: np.array,
        end: np.array,
        camera_mat: np.array
    ) -> None:
        self.camera_mat = camera_mat
        self.start = start
        self.end = end
    
    def get_point(self, t: float) -> np.array:
        start = self.start
        end = self.end
        return start + (t * (end - start))
