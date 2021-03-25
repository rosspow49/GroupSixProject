import unittest

import pygame

from src.Display.IOLogger import IOLogger
from src.Engine.main import playSound


class EngineTest(unittest.TestCase):

    def test_PlaySoundNoCurrentSong(self):
        pygame.mixer.init()
        filePath = "../src/Data/stubMusic/bensound-dubstep.wav"
        logger = IOLogger(False)
        soundPlayer = playSound(filePath, 1, logger)

        self.assertTrue(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_PlaySoundWithSongAlreadyPlaying(self):
        pygame.mixer.init()
        filePath = "../src/Data/stubMusic/bensound-dubstep.wav"
        logger = IOLogger(False)
        soundPlayer = playSound(filePath, 1, logger)
        newsoundPlayer = playSound(filePath, 1, logger)
        self.assertTrue(pygame.mixer.get_busy())

        pygame.mixer.quit()


if __name__ == '__main__':
    unittest.main()
