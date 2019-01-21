#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

img = pygame.image.load('resources/cat.png')
x = y = 100

surface.blit(img, (x, y))

while True: # the main game loop
   # surface.fill((255,0,0,))
   # surface.blit(catImg, (x, y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
