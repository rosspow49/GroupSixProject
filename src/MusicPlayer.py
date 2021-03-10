import pygame
def MusicPlayer(FilePath):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(FilePath)
    pygame.mixer.music.play()
