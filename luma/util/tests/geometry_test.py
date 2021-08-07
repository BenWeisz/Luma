import numpy as np
from unittest import TestCase
from math import sin, cos

from luma.util.geometry import getRotationMatrix, asHomogeneous, asCoordinate

class RotationMatTest(TestCase):
    def test_rotateAll90(self):
        pi_over_two = np.pi / 2.0
        xzx = np.array([pi_over_two, pi_over_two, pi_over_two])

        rot_mat = getRotationMatrix(xzx)
        original_point = np.array([1, 0, 0])
        
        rotated_point = rot_mat.dot(original_point)
        self.assertAlmostEqual(rotated_point[0], 0)
        self.assertAlmostEqual(rotated_point[1], 0)
        self.assertAlmostEqual(rotated_point[2], 1)

    def test_rotate45Z(self):
        pi_over_4 = np.pi / 4.0
        xzx = np.array([0, pi_over_4, 0])
        
        rot_mat = getRotationMatrix(xzx)
        original_point = np.array([1, 0, 0])

        rotated_point = rot_mat.dot(original_point)
        self.assertAlmostEqual(rotated_point[0], cos(pi_over_4))
        self.assertAlmostEqual(rotated_point[1], sin(pi_over_4))
        self.assertAlmostEqual(rotated_point[2], 0)

class AsHomogeneousTest(TestCase):
    def test_asHomogeneous(self):
        vec = np.array([1.0, 2.0, 3.0])
        homogeneous_vec = asHomogeneous(vec)
        self.assertListEqual(
            list(homogeneous_vec),
            [1.0, 2.0, 3.0, 1.0]
        )

class AsCoordinateTest(TestCase):
    def test_asCoordinate(self):
        vec = np.array([2, 2, 2, 2])
        normal_vec = asCoordinate(vec)
        self.assertListEqual(
            list(normal_vec),
            [1, 1, 1]
        )
        
