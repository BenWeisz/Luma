from unittest import TestCase
import numpy as np

from luma.world.entity.entity_types import DirectionalLight, Plane, Sphere
from luma.world.material import Material
from luma.light.ray import Ray
from luma.light.camera import Camera

def get_test_material():
    return Material(
        name="Test Material",
        i_ambient=[255, 0, 0],
        i_diffuse=[0, 255, 0],
        i_specular=[0, 0, 255]
    )

class DirectionalLightTest(TestCase):
    def setUp(self):
        self.material = get_test_material()
        self.directional_light = DirectionalLight(
            name="Test Directional Light",
            direction=[1, 2, 3],
            light=self.material
        )

    def test_init(self):
        self.assertEqual(
            self.directional_light.name,
            "Test Directional Light"
        )
        self.assertListEqual(
            self.directional_light.direction,
            [1, 2, 3]
        )
        self.assertEqual(
            self.directional_light.light,
            self.material
        )

class PlaneTest(TestCase):
    def setUp(self):
        self.material = get_test_material()
        self.plane1 = Plane(
            name="Test Plane",
            point=[1, 2, 3],
            normal=[4, 5, 6],
            material=self.material
        )

        self.plane2 = Plane(
            name="Simple Plane",
            point=[0, 0, 0],
            normal=[0, 0, 1],
            material=self.material
        )

        self.camera = Camera(
            name="Main Camera",
            focal_length=1,
            point=[0, 0, 0],
            xzx=[0, 0, 0],
            window_width=640,
            window_height=480,
            screen_width=1,
            screen_height=1,
        )

        camera_matrix = self.camera.camera_matrix

        self.ray = Ray(
            screen_pos=(0, 0),
            start=[2, 0, 0],
            end=[1, 0, 0],
            camera_mat=camera_matrix
        )

        self.ray_no_intersect = Ray(
            screen_pos=(0, 0),
            start=[0, 0, 1],
            end=[2, 0, 1],
            camera_mat=camera_matrix
        )

        self.ray_inf_intersect = Ray(
            screen_pos=(0, 0),
            start=[0, 0, 0],
            end=[1, 0, 0],
            camera_mat=camera_matrix
        )

    def test_init(self):
        self.assertEqual(
            self.plane1.name,
            "Test Plane"
        )
        self.assertListEqual(
            list(self.plane1.point),
            [1, 2, 3]
        )
        self.assertListEqual(
            list(self.plane1.normal),
            [4, 5, 6]
        )
        self.assertEqual(
            self.plane1.material,
            self.material
        )

    def test_simple_intersect(self):
        self.assertListEqual(
            self.plane1.intersect(self.ray),
            [-6.0]
        )

    def test_no_intersect(self):
        self.assertListEqual(
            self.plane2.intersect(self.ray_no_intersect),
            []
        )

    def test_inf_intersect(self):
        self.assertListEqual(
            self.plane2.intersect(self.ray_inf_intersect),
            [np.inf]
        )

class SphereTest(TestCase):
    def setUp(self):
        self.material = get_test_material()
        self.sphere = Sphere(
            name="Test Sphere",
            point=[1, 2, 3],
            radius=4,
            material=self.material
        )
        self.center_sphere = Sphere(
            "Test Sphere",
            point=[0, 0, 0],
            radius=1,
            material=self.material
        )

        self.camera = Camera(
            name="Main Camera",
            focal_length=1,
            point=[0, 0, 0],
            xzx=[0, 0, 0],
            window_width=640,
            window_height=480,
            screen_width=1,
            screen_height=1,
        )

        self.ray = Ray(
            screen_pos=(0, 0),
            start=[2, 0, 0],
            end=[1, 0, 0],
            camera_mat=self.camera.camera_matrix
        )

    def test_init(self):
        self.assertEqual(
            self.sphere.name,
            "Test Sphere"
        )
        self.assertListEqual(
            self.sphere.point,
            [1, 2, 3]
        )
        self.assertEqual(
            self.sphere.radius,
            4
        )
        self.assertEqual(
            self.sphere.material,
            self.material
        )
        
    def test_intersection(self):
        self.assertSetEqual(
            set(self.center_sphere.intersect(self.ray)),
            set([1, 3])
        )