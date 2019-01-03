#!/usr/bin/python3

import sys, pygame
from pygame.locals import *

FPS = 30

WHITE = (255, 255,255)
BLACK = (0, 0, 0)
RED = (160, 0, 0)
GREEN = (0, 160, 0)
BLUE = (0, 0, 160)
YELLOW = (160, 160, 0)
LIGHTRED = (190, 30, 0)
LIGHTGREEN = (0, 190, 0)
LIGHTBLUE = (0, 0, 190)
LIGHTYELLOW = (190, 190, 0)


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# The size of each square
BOX_SIZE = 20

BOARD_WIDTH, BOARD_HEIGHT = 10, 20


BLANK = '*'

# each shape of dropped piece is bounded in a 5x5 boxes, use 2D array
# to describe them. Shape is arranged in clockwise order.
# long strip
TEMP_WIDTH, TEMP_HEIGHT = 5, 5
SHAPE_I = [ ['**1**', '**1**', '**1**', '**1**', '*****'],
            ['*****', '*****', '1111*', '*****', '*****']]

# J shape
SHAPE_J = [ ['**1**', '**1**', '*11**', '*****', '*****'],
            ['*****', '**1**', '**111', '*****', '*****'],
            ['*****', '*****', '**11*', '**1**', '**1**'],
            ['*****', '*****', '111**', '**1**', '*****']
          ]
# L shape 
SHAPE_L = [ ['*****', '**1**', '111**', '*****', '*****'],
            ['**1**', '**1**', '**11*', '*****', '*****'],
            ['*****', '*****', '**111', '**1**', '*****'],
            ['*****', '*****', '*11**', '**1**', '**1**'] ]

# Square shape
SHAPE_O = [ ['*****', '*11**', '*11**', '*****', '*****']]

# S shape
SHAPE_S = [ ['*****', '*****', '**11*', '*11**', '*****'],
            ['*****', '**1**', '**11*', '***1*', '*****']]
            

SHAPE_T = [ ['*****', '**1**', '*111*', '*****', '*****'],
            ['*****', '**1**', '**11*', '**1**', '*****'],
            ['*****', '*****', '*111*', '**1**', '*****'],
            ['*****', '**1**', '*11**', '**1**', '*****']]

SHAPE_Z = [
            ['*****', '*11**', '**11*', '*****', '*****'],
            ['*****', '**1**', '*11**', '*1***', '*****']]


def draw_box(surf, color,  row, colume, size):
    x = BOX_SIZE * colume
    y = BOX_SIZE * row
    pygame.draw.rect(surf, color, (x, y, size, size))
    pygame.draw.rect(surf, WHITE, (x, y, size, size), 2)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

k = 0
print(SHAPE_L[k])


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # use this to check if the shape_X is OK. When K_UP,
        # expect that the shape will rotate in clockwise.
        if event.type == KEYUP and event.key == K_UP:
            k += 1
            if k == len(SHAPE_L):
                k = 0

    screen.fill(BLACK)
    for h in range(TEMP_HEIGHT):
        for w in range(TEMP_WIDTH):
            if SHAPE_L[k][h][w] != BLANK:
                draw_box(screen, RED, h, w, BOX_SIZE)


    clock.tick(FPS)
    pygame.display.flip()
