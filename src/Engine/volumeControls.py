import pygame


def setVolume(volume, soundPlayer):
    if soundPlayer != "":
        pygame.mixer.Sound.set_volume(soundPlayer, volume)

def getVolume(logger):
    volumeChanged = False
    while not volumeChanged:
        volume = logger.TakeInput("What would you like the volume to be between 0 for mute and 10?")
        try:
            volume = float(volume)
            if volume < 0 or volume > 10:
                raise ValueError

            volume = volume / 10
            volumeChanged = True

        except:
            logger.ShowOutput("This is not a valid number for volume")
    logger.ShowOutput("Volume changed to " + str(volume*10))
    return volume