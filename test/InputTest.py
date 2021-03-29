import unittest

from src.Data.InputDataFile import InputDataFile
from src.Data.InputDataStub import InputDataStub
from src.Engine.main import getPlaylist, playSound
from src.Display.IOLogger import IOLogger
from unittest.mock import MagicMock


class InputTest(unittest.TestCase):
    def test_InputDataFile(self):
        inputType = InputDataFile()
        logger = IOLogger(False)
        playlist = getPlaylist(inputType, "../Music", logger)
        self.assertEqual(playlist[0], "Beat Of Success.mp3")

    def test_InputDataStub(self):
        inputType = InputDataStub()
        logger = IOLogger(False)
        playlist = getPlaylist(inputType, "stubMusic", logger)
        self.assertEqual(playlist[0], "stub_bensound-dubstep.wav")

    def test_getPlaylistFileNotFoundMock(self):
        inputType = InputDataFile()
        directoryPath = "missing file"
        logger = IOLogger(False)
        InputDataFile.getRawData = MagicMock(side_effect=FileNotFoundError)
        playlist = getPlaylist(inputType, directoryPath, logger)
        self.assertEqual(playlist[0], "stub_bensound-dubstep.wav")


if __name__ == '__main__':
    unittest.main()
