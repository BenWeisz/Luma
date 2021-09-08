from typing import List

class World():
    name: str
    body_entities: List['BodyEntity']
    light_entities: List['LightEntity']
    cameras: List['Entity']
    materials: List['Material']

    def __init__(self, name: str) -> None:
        self.name = name
        self.body_entities = []
        self.light_entities = []
        self.cameras = []
        self.materials = []

    def addBodyEntity(self, entity: 'BodyEntity') -> None:
        self.body_entities.append(entity)

    def addLightEntity(self, entity: 'LightEntity') -> None:
        self.light_entities.append(entity)

    def addCamera(self, camera) -> None:
        self.cameras.append(camera)

    def addMaterial(self, material: 'Material') -> None:
        self.materials.append(material)
