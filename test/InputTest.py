import unittest

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Engine.main import getPlaylist


class InputTest(unittest.TestCase):
    def test_InputDataFile(self):
        inputType = InputDataFile()
        playlist = getPlaylist(inputType, "../Music")
        self.assertEqual(playlist[0], "Beat Of Success.mp3")

    def test_InputDataStub(self):
        inputType = InputDataStub()
        playlist = getPlaylist(inputType, "stubMusic")
        self.assertEqual(playlist[0], "bensound-dubstep.wav")


if __name__ == '__main__':
    unittest.main()
