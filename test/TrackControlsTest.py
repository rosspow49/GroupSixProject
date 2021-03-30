import unittest

import pygame

from src.Display.IOLogger import IOLogger
from src.Engine.trackControls import playSound, stopSound


class TrackControlsTest(unittest.TestCase):
    def test_PlaySoundWithNoSongPlaying(self):
        pygame.mixer.init()
        filePath = "../src/Data/stubMusic/stub_bensound-dubstep.wav"
        logger = IOLogger(False)
        soundPlayer = playSound(filePath, 1, logger)
        self.assertTrue(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_PlaySoundWithSongPlaying(self):
        pygame.mixer.init()
        filePath = "../src/Data/stubMusic/stub_bensound-dubstep.wav"
        logger = IOLogger(False)
        soundPlayer = playSound(filePath, 1, logger)
        newsoundPlayer = playSound(filePath, 1, logger)
        self.assertTrue(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_stopSoundWithSongPlaying(self):
        pygame.mixer.init()
        filePath = "../src/Data/stubMusic/stub_bensound-dubstep.wav"
        logger = IOLogger(False)
        soundPlayer = playSound(filePath, 1, logger)
        stopSound(soundPlayer, logger)
        self.assertFalse(pygame.mixer.get_busy())

        pygame.mixer.quit()

    def test_stopSoundWithNoSongPlaying(self):
        pygame.mixer.init()
        filePath = "../src/Data/stubMusic/stub_bensound-dubstep.wav"
        logger = IOLogger(False)
        soundPlayer = playSound(filePath, 1, logger)
        soundPlayer.stop()
        stopSound(soundPlayer, logger)
        self.assertFalse(pygame.mixer.get_busy())

        pygame.mixer.quit()



if __name__ == '__main__':
    unittest.main()
