import pygame

from src.Engine.volumeControls import setVolume
musicPlaying = True

def playSound(filePath, volume, logger):
    pygame.mixer.stop()
    soundPlayer = pygame.mixer.Sound(filePath)
    setVolume(volume, soundPlayer)
    soundPlayer.play()
    print("Now playing: " + filePath)

    return soundPlayer


def stopSound(soundPlayer, logger):
    if pygame.mixer.get_busy():
        soundPlayer.stop()
        logger.ShowOutput("Song stopped.")
    else:
        logger.ShowOutput("There is no song playing at the moment")


def playPause(logger):
    global musicPlaying

    if pygame.mixer.get_busy():

        if musicPlaying:
            musicPlaying = False
            pygame.mixer.pause()
            logger.ShowOutput("Pausing Song")
        else:
            musicPlaying = True
            pygame.mixer.unpause()
            logger.ShowOutput("Resuming song")



