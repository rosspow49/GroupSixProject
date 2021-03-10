import pygame

pygame.mixer.init()
s = pygame.mixer.Sound("bensound-dubstep.wav")
s.play()
pygame.time.wait(100000)
