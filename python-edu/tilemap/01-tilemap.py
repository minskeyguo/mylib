#!/usr/bin/python3


import pygame
from pygame.locals import *


BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
GOLD = 3

colors = { DIRT:BROWN, GRASS:GREEN, WATER:BLUE, GOLD:BLACK }

tilemap = [ [GRASS, GOLD, DIRT], [WATER, GRASS, WATER], 
            [GOLD, GRASS, WATER], [DIRT, GRASS, GOLD],
            [GRASS, WATER, DIRT] ]

TILESIZE = 40
MAP_WIDTH=3
MAP_HEIGHT=5

pygame.init()
screen = pygame.display.set_mode((MAP_WIDTH * TILESIZE, MAP_HEIGHT * TILESIZE))

textures = {
        DIRT:pygame.image.load('images/dirt.png').convert(),
        GRASS:pygame.image.load('images/grass.png').convert(),
        WATER:pygame.image.load('images/brick.png').convert(),
        GOLD:pygame.image.load('images/gold.png').convert(),
        }


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            # pygame.draw.rect(screen, colors[tilemap[row][col]], (TILESIZE * col, TILESIZE * row, TILESIZE, TILESIZE))
            screen.blit(textures[tilemap[row][col]], (TILESIZE * col, TILESIZE * row, TILESIZE, TILESIZE))

    pygame.display.update()

