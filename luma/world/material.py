from typing import Iterable

class Material:
    def __init__(
        self,
        name: str,
        i_ambient: Iterable,
        i_diffuse: Iterable,
        i_specular: Iterable,
        phong_coeff: float
    ) -> None:
        self.name = name
        self.i_ambient = i_ambient
        self.i_diffuse = i_diffuse
        self.i_specular = i_specular
        self.phong_coeff = phong_coeff
