import unittest

from src.Display.IOTest import IOTest
from src.Engine.volumeControls import getVolume
from unittest.mock import MagicMock


class GetVolumeTest(unittest.TestCase):
    def test_getValidVolume(self):
        logger = IOTest()
        logger.SetInputList([5])
        self.assertEqual(0.5, getVolume(logger))

    def test_getMinVolume(self):
        logger = IOTest()
        logger.SetInputList([0])
        self.assertEqual(0, getVolume(logger))

    def test_getMaxVolume(self):
        logger = IOTest()
        logger.SetInputList([10])
        self.assertEqual(1, getVolume(logger))

    def test_getOutOfBoundsVolume(self):
        logger = IOTest()
        logger.SetInputList([-1, 5])
        self.assertEqual(0.5, getVolume(logger))

    def test_getInvalidVolume(self):
        logger = IOTest()
        logger.SetInputList(["", 5])
        self.assertEqual(0.5, getVolume(logger))

    def test_getNullVolume(self):
        logger = IOTest()
        logger.SetInputList([None, 5])
        self.assertEqual(0.5, getVolume(logger))

    def test_getMultipleVolumesMock(self):
        logger = IOTest()
        logger.TakeInput = MagicMock(side_effect=[5, 10, 0])
        self.assertEqual(0.5, getVolume(logger))
        self.assertEqual(1, getVolume(logger))
        self.assertEqual(0, getVolume(logger))



if __name__ == '__main__':
    unittest.main()
