import pygame

def playSound(filePath, volume, logger):
    pygame.mixer.stop()
    soundPlayer = pygame.mixer.Sound(filePath)
    pygame.mixer.Sound.set_volume(soundPlayer, volume)
    soundPlayer.play()
    print("Now playing: " + filePath)

    return soundPlayer


def stopSound(soundPlayer, logger):
    if pygame.mixer.get_busy():
        soundPlayer.stop()
        logger.ShowOutput("Song stopped.")
    else:
        logger.ShowOutput("There is no song playing at the moment")