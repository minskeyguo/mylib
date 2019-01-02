#!/usr/bin/python3

import sys, pygame, random
from pygame.locals import *

FPS = 30

WHITE = (255, 255,255)
BLACK = (0, 0, 0)
RED = (160, 0, 0)
GREEN = (0, 160, 0)
BLUE = (0, 0, 160)
YELLOW = (160, 160, 0)
GRAY = (100, 100, 100)
LIGHTRED = (190, 30, 0)
LIGHTGREEN = (0, 190, 0)
LIGHTBLUE = (0, 0, 190)
LIGHTYELLOW = (190, 190, 0)
COLORS = [WHITE, BLACK, RED, GREEN, BLUE, YELLOW] 


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480


# The size of each square
BOX_SIZE = 20

BOARD_WIDTH, BOARD_HEIGHT = 8, 20


X_MARGIN = (SCREEN_WIDTH - BOARD_WIDTH * BOX_SIZE) // 2
Y_MARGIN = SCREEN_HEIGHT - BOARD_HEIGHT * BOX_SIZE - 8

PIECE_DOWN_FREQ = 180

BLANK = '*'

# each shape of dropped piece is bounded in a 5x5 boxes, use 2D array
# to describe them. Shape is arranged to rotate in clockwise order.And
# the center is (2,2)
TEMP_WIDTH, TEMP_HEIGHT = 5, 5

# long strip
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


SHAPE_LIST = [SHAPE_I, SHAPE_J, SHAPE_L, SHAPE_O, SHAPE_S, SHAPE_T, SHAPE_Z]

def draw_box(surf, color, row, colume, size):
    x_pix = X_MARGIN +  BOX_SIZE * colume 
    y_pix = Y_MARGIN + BOX_SIZE * row
    pygame.draw.rect(surf, COLORS[color], (x_pix, y_pix, size, size))
    pygame.draw.rect(surf, RED, (x_pix, y_pix, size, size), 2)

def new_piece():
    shape = random.choice(SHAPE_LIST)
    piece = { 'shape':shape,
              'index':random.randint(0, len(shape) - 1),
              'x': BOARD_WIDTH // 2 - 5 //2,
              'y': -5,   # just let 5x5 template locate right above the board
              'color': random.randint(0, len(COLORS) - 1)}
    return piece

def draw_piece(screen, piece, x_pos, y_pos):
    shape = piece['shape'][piece['index']]
    for y in range(TEMP_HEIGHT):
        for x in range(TEMP_WIDTH):
            if shape[y][x] != BLANK:
                draw_box(screen, piece['color'], y_pos + y, x_pos + x, BOX_SIZE)

def draw_board( ):
    pygame.draw.rect(screen, BLUE, (X_MARGIN, Y_MARGIN, BOARD_WIDTH * BOX_SIZE, BOARD_HEIGHT *BOX_SIZE))
    pygame.draw.rect(screen, RED, (X_MARGIN, Y_MARGIN, BOARD_WIDTH * BOX_SIZE, BOARD_HEIGHT *BOX_SIZE), 2)


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

curr_piece = new_piece()
piece_last_down_time = pygame.time.get_ticks()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == KEYUP and event.key == K_UP:

    now = pygame.time.get_ticks()
    if now - piece_last_down_time > PIECE_DOWN_FREQ:
        curr_piece['y'] += 1
        piece_last_down_time = now

    screen.fill(BLACK)
    draw_board( )
    draw_piece(screen, curr_piece, curr_piece['x'], curr_piece['y'])
    
    pygame.display.flip()
    clock.tick(FPS)
