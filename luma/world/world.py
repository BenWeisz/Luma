from luma.world.entity.entity import Entity
from luma.world.material import Material

class World():
    def __init__(self, name):
        self.name = name
        self.entities = []
        self.materials = []

    def addEntity(self, entity: Entity) -> None:
        self.entities.append(entity)

    def addMaterial(self, material: Material) -> None:
        self.materials.append(material)
