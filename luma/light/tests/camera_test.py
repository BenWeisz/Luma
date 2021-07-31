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
