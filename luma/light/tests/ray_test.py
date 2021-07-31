from unittest import TestCase
import numpy as np

from luma.light.ray import Ray

class RayTest(TestCase):
    def setUp(self) -> None:
        self.ray = Ray(
            np.array([0, 0, 0]),
            np.array([2, 0, 0])
        )

    def test_fullDistance(self):
        point = self.ray.get_point(1.0)
        dist_to_point = np.sum(point - np.array([2, 0, 0]))
        self.assertEqual(0, dist_to_point)

    def test_doubleDistance(self):
        point = self.ray.get_point(2.0)
        dist_to_point = np.sum(point - np.array([4, 0, 0]))
        self.assertEqual(0, dist_to_point)
