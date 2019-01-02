#!/usr/bin/python3


import pygame
import random
import sys
from pygame.locals import *


BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)

DIRT = 0
GRASS = 1
WATER = 2
GOLD = 3

resources = [ DIRT, GRASS, WATER, GOLD ]
colors = { DIRT:BROWN, GRASS:GREEN, WATER:BLUE, GOLD:BLACK }

TILESIZE = 40
MAP_WIDTH=30
MAP_HEIGHT=30

pygame.init()
screen = pygame.display.set_mode((MAP_WIDTH * TILESIZE, MAP_HEIGHT * TILESIZE))

tilemap = [ [ random.choice(resources) for w in range(MAP_WIDTH)] for h in range(MAP_HEIGHT) ]
for w in range(MAP_WIDTH):
    for h in range(MAP_HEIGHT):
        i = random.randint(0, 15)
        if i == 0:
            tilemap[w][h] = GOLD
        elif i == 1 or i == 2:
            tilemap[w][h] = WATER
        elif i <=7:
            tilemap[w][h] = GRASS
        else:
            tilemap[w][h] = DIRT

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

