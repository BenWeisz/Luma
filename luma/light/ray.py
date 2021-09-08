from typing import Iterable, Tuple, List
import numpy as np
from numpy.linalg import norm

from luma.util.geometry import asCoordinate, asHomogeneous
from luma.world.world import World

DIRECTIONAL_LIGHT = "DirectionalLight"
Intersection = Tuple[float, 'BodyEntity']

class Ray():
    start: np.array
    end: np.array
    screen_pos: Tuple[int, int]
    intersections: List[Intersection]

    def __init__(
        self,
        screen_pos: Iterable,
        start: np.array,
        end: np.array,
        camera_mat: np.array
    ) -> None:
        self.screen_pos = tuple(screen_pos)

        if camera_mat is not None:
            self.start = asCoordinate(camera_mat.dot(asHomogeneous(start)))
            self.end = asCoordinate(camera_mat.dot(asHomogeneous(end)))
        else:
            self.start = start
            self.end = end
    
    def get_point(self, t: float) -> np.array:
        start = self.start
        end = self.end
        return start + (t * (end - start))

    @staticmethod
    def prune_intersections(intersections: List[Intersection]) -> List[Intersection]:
        pruned_intersections = list(filter(lambda x: x[0] >= 1, intersections))
        pruned_intersections.sort(
            reverse=False,
            key=lambda x: x[0]
        )
        
        return pruned_intersections

    def set_intersections(self, intersections: List[Intersection]) -> None:
        self.intersections = intersections

    def get_intersection_color(self, world: World) -> np.array:
        """ Get the color of associated with the ray given the
            intersections with the BodyEntities in the world.

            Assumption: set_intersections has been called.
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


            # TODO fix this because the direction seems a bit off
            viewing_dir = self.start - self.end
            viewing_dir = viewing_dir / np.linalg.norm(viewing_dir)
            viewing_dir *= -1

            color_specular = np.zeros(3)
            for light in world.light_entities:
                if light.__class__.__name__ == DIRECTIONAL_LIGHT:
                    #r = (2 * normal) + light.direction
                    r = (2 * normal.dot(light.direction) * normal) - light.direction
                    r = r / np.linalg.norm(r)
                    intensity = max([0, r.dot(viewing_dir)])**closest_body.material.phong_coeff
                    color_specular += (light.light.i_ambient / 255.0) * intensity

            color = color_ambient
            if not self.is_in_shadow(light, world):
                color += color_diffuse + color_specular

        return np.clip(color * 255.0, 0, 255)

    def is_in_shadow(self, light: 'LightBody', world: 'World') -> bool:
        """ Check if the first intersection point is shadowed
            by objects with respect to a particular light source.

            Assumption: set_intersections has been called.
        """
        
        t, closest_body = self.intersections[0]    
        t_point = self.get_point(t)
        normal = closest_body.get_normal(t_point)

        SHADOW_EPSILON = 0.001
        ray_start = t_point + (SHADOW_EPSILON * normal)
        if light.__class__.__name__ == DIRECTIONAL_LIGHT:
            ray_end = ray_start - light.direction

        ray = Ray(
            screen_pos=[],
            start=ray_start,
            end=ray_end,
            camera_mat=None
        )

        intersections = []
        for ent in world.body_entities:
            ent_ray_intersections = ent.intersect(ray)
            ent_ray_intersections = map(lambda t: (t, ent), ent_ray_intersections)
            intersections.extend(list(ent_ray_intersections))
        intersections = Ray.prune_intersections(intersections)

        return len(intersections) > 0
