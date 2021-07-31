import numpy as np

class Ray():
    start: np.array
    end: np.array

    def __init__(
        self,
        start: np.array,
        end: np.array
    ) -> None:
        self.start = start
        self.end = end
    
    def get_point(self, t):
        start = self.start
        end = self.end
        return start + (t * (end - start))
