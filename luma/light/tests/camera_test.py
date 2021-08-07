from unittest import TestCase
import numpy as np

from luma.light.camera import Camera

class CameraTest(TestCase):
    def setUp(self) -> None:
        self.camera = Camera(
            name="Test",
            point=[1, 2, 3],
            xzx=[1, 2, 3],
            focal_length=1,
            window_width=2,
            window_height=3,
            screen_width=4,
            screen_height=5,
        )

    def test_init(self):
        self.assertEqual(
            self.camera.name,
            "Test"
        )
        self.assertEqual(
            0,
            np.sum(self.camera.point - np.array([1, 2, 3]))
        )
        self.assertEqual(
            0,
            np.sum(
                self.camera.xzx -
                np.array([1, 2, 3])
            )
        )
        self.assertEqual(
            self.camera.focal_length,
            1
        )
        self.assertEqual(
            self.camera.window_width,
            2
        )
        self.assertEqual(
            self.camera.window_height,
            3
        )
        self.assertEqual(
            self.camera.screen_width,
            4
        )
        self.assertEqual(
            self.camera.screen_height,
            5
        )

    def test_camera_matrix(self):
        camera_mat = self.camera.camera_matrix
        row1_sum = np.sum(np.array([-0.41614684, -0.4912955, 0.7651474, 1]) - camera_mat[0])
        row2_sum = np.sum(np.array([-0.90019763, 0.10384657, -0.42291857, 2]) - camera_mat[1])
        row3_sum = np.sum(np.array([0.12832006, -0.8647801, -0.48547846, 3]) - camera_mat[2])
        row4_sum = np.sum(np.array([0, 0, 0, 1]) - camera_mat[3])

        self.assertAlmostEqual(row1_sum, 0)
        self.assertAlmostEqual(row2_sum, 0)
        self.assertAlmostEqual(row3_sum, 0)
        self.assertAlmostEqual(row4_sum, 0)