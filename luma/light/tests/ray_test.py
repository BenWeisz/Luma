from unittest import TestCase
import numpy as np

from luma.light.ray import Ray
from luma.light.camera import Camera

class RayTest(TestCase):
    def setUp(self) -> None:
        self.camera = Camera(
            name='Main Camera',
            point=[0, 0, 0],
            xzx=[0, 0, 0],
            focal_length=1,
            window_width=640,
            window_height=480,
            screen_width=1,
            screen_height=1,
        )
        self.ray = Ray(
            screen_pos=(0, 0),
            start=np.array([0, 0, 0]),
            end=np.array([2, 0, 0]),
            camera_mat=self.camera.camera_matrix
        )

    def test_fullDistance(self):
        point = self.ray.get_point(1.0)
        dist_to_point = np.sum(point - np.array([2, 0, 0]))
        self.assertEqual(0, dist_to_point)

    def test_doubleDistance(self):
        point = self.ray.get_point(2.0)
        dist_to_point = np.sum(point - np.array([4, 0, 0]))
        self.assertEqual(0, dist_to_point)
