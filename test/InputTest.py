import unittest

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Engine.main import getPlaylist, playSound
from src.Display.IOLogger import IOLogger


class InputTest(unittest.TestCase):
    def test_InputDataFile(self):
        inputType = InputDataFile()
        playlist = getPlaylist(inputType, "../Music")
        self.assertEqual(playlist[0], "Beat Of Success.mp3")

    def test_InputDataStub(self):
        inputType = InputDataStub()
        playlist = getPlaylist(inputType, "stubMusic")
        self.assertEqual(playlist[0], "bensound-dubstep.wav")

    def test_findFile(self):
        filePath = "bensound-dubstep.wav"
        directoryPath = "../Music/"
        volume = 1
        logger = IOLogger(False)
        try:
            playSound(directoryPath + filePath, volume, logger)
        except FileNotFoundError:
            self.assertRaises(FileNotFoundError, playSound(directoryPath + filePath, volume, logger))




if __name__ == '__main__':
    unittest.main()
