from typing import Iterable

from luma.world.material import Material

class Entity:
    def __init__(self, name: str) -> None:
        self.name = name

class DirectionalLight(Entity):
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
