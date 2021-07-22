from typing import Iterable

class Material:
    def __init__(
        self,
        name: str,
        i_ambient: Iterable,
        i_diffuse: Iterable,
        i_specular: Iterable,
    ) -> None:
        self.name = name
        self.i_ambient = i_ambient
        self.i_diffuse = i_diffuse
        self.i_specular = i_specular
