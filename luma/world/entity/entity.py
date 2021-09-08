from typing import List

import numpy as np

from luma.light.ray import Ray
from luma.world.material import Material

class Entity:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

class BodyEntity(Entity):
    material: Material

    def __init__(self, name: str, material: Material) -> None:
        super().__init__(name)
        self.material = material

    def get_normal(self, point: np.array) -> np.array:
        """ Get the normal for the BodyEntity at the given point.
        
            Assumption: the point lies on the BodyEntity's surface.
        """
        pass

    def intersect(self, ray: Ray) -> List[float]:
        """ Intersect the given ray with the BodyEntity.
        """
        pass

class LightEntity(Entity):
    light: Material

    def __init__(self, name: str, light: Material) -> None:
        super().__init__(name)
        self.light = light
