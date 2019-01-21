#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()

# set up the window
surface = pygame.display.set_mode((640, 300), 0, 32)
pygame.display.set_caption('Font')

font1 = pygame.font.Font("freesansbold.ttf", 32)
# render(text, antialias, color, background=None)
ts1 = font1.render("This is a font test", True, GREEN, BLUE)
tr1 = ts1.get_rect()
tr1.center = (320, 15)

font2 = pygame.font.Font(None, 64)
ts2 = font2.render("this is 64# font", True, RED)

while True:
   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

   surface.fill(WHITE)
   surface.blit(ts1, tr1)

   surface.blit(ts2, (0, 100))

   # make the context visable
   pygame.display.update()
