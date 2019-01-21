#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

pygame.init()

# 
sound = pygame.mixer.Sound("hell.wav")
sound.play()
sound.stop()

# background music
pygame.mixer.music.load()
pygame.mixer.music.play(−1, 0.0)   # (repeat-times, beginning-time-in-file)
pygame.mixer.music.stop()   # (repeat-times, beginning-time-in-file)

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Font')

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
