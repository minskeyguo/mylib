#!/usr/bin/python3

import sys, pygame
from pygame.locals import *


black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
pygame.init()

pygame.display.set_caption("drawing") # set the title of the window
surface = pygame.display.set_mode((400, 300)) # return pygame.Surface

surface.fill(white)    #  <=== white the surface


# how to modify single pixel of a surfce:
po = pygame.PixelArray(surface)  # it will lock surface
po[200][150] = red
po[201][150] = red

po[200][155] =  green
po[201][155] =  green

po[200][160] =  blue
po[201][160] =  blue

po[200][165] =  black
po[201][165] =  black

del po     # unlock the surface


# event loop: handling event, update game state(variables), rendering graphics
while True:
    for event in pygame.event.get():

        # QUIT etc, defined in pygame.locals
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()
    pygame.display.update()  # render surface into screen




"""
Surface:   2D rectangle

Color : (r, g, b, a)

Rect: (x0, y0, width, height)
"""
            
