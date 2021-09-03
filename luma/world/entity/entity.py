from typing import List

from luma.light.ray import Ray

class Entity:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def intersect(self, ray: Ray) -> List[float]:
        return []
