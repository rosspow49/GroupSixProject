import pygame


def setVolume(volume, soundPlayer):
    if soundPlayer != "":
        pygame.mixer.Sound.set_volume(soundPlayer, volume)

def getVolume(logger):
    volumeChanged = False
    while not volumeChanged:
        volume = logger.takeInput("What would you like the volume to be between 0 for mute and 10?")
        try:
            volume = float(volume)
            if volume < 0 or volume > 10:
                raise ValueError

            logger.showOutput("Volume changed to " + str(volume))
            volume = volume / 10
            volumeChanged = True
        except:
            logger.showOutput("This is not a valid number for volume")
    return volume