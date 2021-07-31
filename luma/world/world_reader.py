import json
from typing import Dict, List
import numpy as np

from luma.world.entity.entity import Entity
from luma.world.entity.entity_types import Plane, Sphere, DirectionalLight
from luma.world.material import Material
from luma.light.camera import Camera

from .world import World

class WorldReader():
    @staticmethod
    def read(path: str) -> World:
        with open(f"data/in/{path}", "r") as input_file:
            json_data = json.load(input_file)
            
            world = World(name=json_data["name"])

            for material in json_data["materials"]:
                new_material = WorldReader.parseMaterial(material=material)
                world.addMaterial(new_material)

            for entity in json_data["entities"]:
                new_entity = WorldReader.parseEntity(
                    entity=entity,
                    materials=world.materials
                )
                world.addEntity(new_entity)

        return world

    @staticmethod
    def parseMaterial(material: Dict) -> Material:
        return Material(
            name=material["name"],
            i_ambient=np.array(material["i_ambient"]),
            i_diffuse=np.array(material["i_diffuse"]),
            i_specular=np.array(material["i_specular"]),
        )

    @staticmethod
    def parseEntity(entity: Dict, materials: List[Material]) -> Entity:
        entity_type = entity["type"]
        if entity_type == Plane.__name__:
            return Plane(
                name=entity["name"],
                point=np.array(entity["point"]),
                normal=np.array(entity["normal"]),
                material=materials[entity["material"]],
            )
        elif entity_type == Sphere.__name__:
            return Sphere(
                name=entity["name"],
                point=np.array(entity["point"]),
                radius=entity["radius"],
                material=materials[entity["material"]],
            )
        elif entity_type == DirectionalLight.__name__:
            return DirectionalLight(
                name=entity["name"],
                direction=np.array(entity["direction"]),
                material=materials[entity["material"]],
            )
        elif entity_type == Camera.__name__:
            return Camera(
                name="Main Camera",
                point=np.array(entity["point"]),
                direction=np.array(entity["direction"]),
                focal_length=entity["focalLength"],
                window_width=entity["windowWidth"],
                window_height=entity["windowHeight"],
                screen_width=entity["screenWidth"],
                screen_height=entity["screenHeight"],
            )
