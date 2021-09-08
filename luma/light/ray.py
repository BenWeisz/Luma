from typing import Iterable, Tuple, List
import numpy as np

from luma.util.geometry import asCoordinate, asHomogeneous
from luma.world.world import World

DIRECTIONAL_LIGHT = "DirectionalLight"

class Ray():
    start: np.array
    end: np.array
    screen_pos: Tuple[int, int]
    intersections: List[Tuple[float, 'BodyEntity']]

    def __init__(
        self,
        screen_pos: Iterable,
        start: np.array,
        end: np.array,
        camera_mat: np.array
    ) -> None:
        self.screen_pos = tuple(screen_pos)
        self.start = asCoordinate(camera_mat.dot(asHomogeneous(start)))
        self.end = asCoordinate(camera_mat.dot(asHomogeneous(end)))
    
    def get_point(self, t: float) -> np.array:
        start = self.start
        end = self.end
        return start + (t * (end - start))

    def set_and_sort_intersections(self, intersections: List[Tuple[float, 'BodyEntity']]) -> None:
        self.intersections = intersections
        self.intersections.sort(
            reverse=False,
            key=lambda x: x[0]
        )

    def get_intersection_color(self, world: World) -> np.array:
        """ Get the color of associated with the ray given the
            intersections with the BodyEntities in the world.

            Assumption: set_and_sort_intersections has been called.
        """

        color = np.zeros(3)
        if len(self.intersections):            
            t, closest_body = self.intersections[0]    
            t_point = self.get_point(t)
            normal = closest_body.get_normal(t_point)
            
            color_ambient = (closest_body.material.i_ambient / 255.0) * 0.25
            color_diffuse = np.zeros(3)
            for light in world.light_entities:
                if light.__class__.__name__ == DIRECTIONAL_LIGHT:
                    intensity = max([0, normal.dot(-light.direction)])
                    color_diffuse += (closest_body.material.i_diffuse / 255.0) * (light.light.i_ambient / 255.0) * intensity


            viewing_dir = self.start - self.end
            viewing_dir = viewing_dir / np.linalg.norm(viewing_dir)
            viewing_dir *= -1

            color_specular = np.zeros(3)
            for light in world.light_entities:
                if light.__class__.__name__ == DIRECTIONAL_LIGHT:
                    #r = (2 * normal) + light.direction
                    r = (2 * normal.dot(light.direction) * normal) - light.direction
                    r = r / np.linalg.norm(r)
                    intensity = max([0, r.dot(viewing_dir)])**20
                    color_specular += (light.light.i_ambient / 255.0) * intensity

            color = color_ambient + color_diffuse + color_specular

        return np.clip(color * 255.0, 0, 255)
