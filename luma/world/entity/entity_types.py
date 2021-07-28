from typing import Iterable

from luma.world.entity.entity import Entity
from luma.world.material import Material

class DirectionalLight(Entity):
    name: str
    direction: Iterable
    material: Material

    def __init__(
        self,
        name: str,
        direction: Iterable,
        material: Material
    ) -> None:
        super().__init__(name)
        self.directon = direction
        self.material = material

class Plane(Entity):
    name: str
    point: Iterable
    normal: Iterable
    material: Material

    def __init__(
        self,
        name: str,
        point: Iterable,
        normal: Iterable,
        material: Material
    ) -> None:
        super().__init__(name)
        self.point = point
        self.normal = normal
        self.material = material

class Sphere(Entity):
    name: str
    point: Iterable
    radius: float
    material: Material

    def __init__(
        self,
        name: str,
        point: Iterable,
        radius: float,
        material: Material
    ) -> None:
        super().__init__(name)
        self.point = point
        self.radius = radius
        self.material = material
