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

# draw polygon
pygame.draw.polygon(surface, green, ((123, 0), (234,132), (269, 211), (77, 66)), 0)

# draw line
pygame.draw.line(surface, red, (70, 200), (80,100), 20)

pygame.draw.circle(surface, black, (30, 50), 15, 10)
pygame.draw.ellipse(surface, black, (30, 50, 100, 60), 10)

pygame.draw.rect(surface, blue, (30, 50, 100, 60))



# event loop: handling event, update game state(variables), rendering graphics
while True:
    for event in pygame.event.get():

        # QUIT etc, defined in pygame.locals
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()
    pygame.display.update()  # render surface into screen


# Question:
# what's the different if we move Line 14 ~ 18 into loop before pygame.display.update() ?

"""
Surface:   2D rectangle

Color : (r, g, b, a)

Rect: (x0, y0, width, height)
"""
            
