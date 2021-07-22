from unittest import TestCase
from luma.world.entity import DirectionalLight, Plane, Sphere
from luma.world.material import Material

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
            material=self.material
        )

    def test_init(self):
        self.assertEqual(
            self.directional_light.name,
            "Test Directional Light"
        )
        self.assertListEqual(
            self.directional_light.directon,
            [1, 2, 3]
        )
        self.assertEqual(
            self.directional_light.material,
            self.material
        )

class PlaneTest(TestCase):
    def setUp(self):
        self.material = get_test_material()
        self.plane = Plane(
            name="Test Plane",
            point=[1, 2, 3],
            normal=[4, 5, 6],
            material=self.material
        )

    def test_init(self):
        self.assertEqual(
            self.plane.name,
            "Test Plane"
        )
        self.assertListEqual(
            self.plane.point,
            [1, 2, 3]
        )
        self.assertListEqual(
            self.plane.normal,
            [4, 5, 6]
        )
        self.assertEqual(
            self.plane.material,
            self.material
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