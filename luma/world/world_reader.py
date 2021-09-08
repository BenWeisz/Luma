import json
from typing import Dict, List
import numpy as np

from luma.world.entity.entity import BodyEntity, LightEntity
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

            for e in json_data["body_entities"]:
                body_entity = WorldReader.parseBodyEntity(
                    entity=e,
                    materials=world.materials
                )
                world.addBodyEntity(body_entity)

            for e in json_data["light_entities"]:
                light_entity = WorldReader.parseLightEntity(
                    entity=e,
                    materials=world.materials
                )
                world.addLightEntity(light_entity)

            for c in json_data["cameras"]:
                camera = WorldReader.parseCamera(c)
                world.addCamera(camera)

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
    def parseBodyEntity(entity: Dict, materials: List[Material]) -> BodyEntity:
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

    @staticmethod
    def parseLightEntity(entity: Dict, materials: List[Material]) -> LightEntity:
        entity_type = entity["type"]
        if entity_type == DirectionalLight.__name__:
            return DirectionalLight(
                name=entity["name"],
                direction=np.array(entity["direction"]),
                light=materials[entity["material"]],
            )

    @staticmethod
    def parseCamera(entity: Dict) -> Camera:
        return Camera(
            name="Main Camera",
            point=np.array(entity["point"]),
            xzx=np.array(entity["xzx"]),
            focal_length=entity["focalLength"],
            window_width=entity["windowWidth"],
            window_height=entity["windowHeight"],
            screen_width=entity["screenWidth"],
            screen_height=entity["screenHeight"],
        )
