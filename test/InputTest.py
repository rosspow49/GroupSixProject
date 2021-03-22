import unittest

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.main import getPlaylist


class InputTest(unittest.TestCase):
    def test_InputDataFile(self):
        inputType = InputDataFile()
        playlist = getPlaylist(inputType)
        self.assertEqual(playlist[1], "bensound-dubstep.wav")

    def test_InputDataStub(self):
        inputType = InputDataStub()
        playlist = getPlaylist(inputType)
        self.assertEqual(playlist[0], "track1")


if __name__ == '__main__':
    unittest.main()
