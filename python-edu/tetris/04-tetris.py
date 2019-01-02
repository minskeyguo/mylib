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


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 800


# The size of each square
BOX_SIZE = 20

BOARD_WIDTH, BOARD_HEIGHT = 12, 25 


X_MARGIN = (SCREEN_WIDTH - BOARD_WIDTH * BOX_SIZE) // 2
Y_MARGIN = SCREEN_HEIGHT - BOARD_HEIGHT * BOX_SIZE - 8

PIECE_MOVE_FREQ = 100
PIECE_DOWN_FREQ = 200
PIECE_ROTATE_FREQ = 250 

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
    if color == BLANK: return
    x_pix = X_MARGIN +  BOX_SIZE * colume
    y_pix = Y_MARGIN + BOX_SIZE * row
    pygame.draw.rect(surf, COLORS[color], (x_pix, y_pix, size, size))
    pygame.draw.rect(surf, GRAY, (x_pix, y_pix, size, size), 2)

# define board as boxes of h rows X w colume
def init_board(w, h):
    board = []
    for i in range(h):
        board.append([BLANK] * w)
    return board

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

def draw_board(board):
    pygame.draw.rect(screen, GRAY, (X_MARGIN, Y_MARGIN, BOARD_WIDTH * BOX_SIZE, BOARD_HEIGHT *BOX_SIZE))
    pygame.draw.rect(screen, RED, (X_MARGIN, Y_MARGIN, BOARD_WIDTH * BOX_SIZE, BOARD_HEIGHT *BOX_SIZE), 2)
    for h in range(BOARD_HEIGHT):
        for w in range(BOARD_WIDTH):
            draw_box(screen, board[h][w], h, w, BOX_SIZE)

def isOnBoard(x, y):
    return x >= 0 and x < BOARD_WIDTH and y < BOARD_HEIGHT

def validate_pos(board, piece, x_off=0, y_off=0):
    for h in range(TEMP_HEIGHT):
        for w in range(TEMP_WIDTH):

            # blank box
            if piece['shape'][piece['index']][h][w] == BLANK: continue

            # above the board
            if (piece['y'] + h + y_off ) < 0: continue

            if not isOnBoard(piece['x'] + w + x_off, piece['y'] + h + y_off):
                return False

            if board[piece['y'] + h + y_off][piece['x'] + w + x_off] != BLANK:
                return False
    return True

def addToBoard(board, piece):
    for y in range(TEMP_HEIGHT):
        for x in range(TEMP_WIDTH):
            if piece['shape'][piece['index']][y][x] != BLANK:
                board [piece['y'] + y][piece['x'] + x] = piece['color']

def remove_competed_lines(board, y_pos):
    for i  in range (TEMP_HEIGHT):
        y = y_pos + i
        if y >= BOARD_HEIGHT:
            break
        completed = True
        for x in range(BOARD_WIDTH):
            if board[y][x] == BLANK:
                completed = False
                break;

        if completed == True:
            y = min(y_pos + 4, BOARD_HEIGHT -1)
            for yboard in range(y, 0, -1):
                for xboard in range(BOARD_WIDTH):
                    board[yboard][xboard] = board[yboard - 1][xboard]
            board[0] = [BLANK] * BOARD_WIDTH
            
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board = init_board(BOARD_WIDTH, BOARD_HEIGHT)
curr_piece = new_piece()
next_piece = new_piece()

piece_last_down_time = pygame.time.get_ticks()
piece_last_rotate_time = pygame.time.get_ticks()
piece_last_move = pygame.time.get_ticks()

offset = { K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0, K_SPACE:0 }

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            offset[event.key] = 0
        elif event.type == KEYDOWN:
            offset[event.key] = 1

    speedx = offset[K_RIGHT] - offset [K_LEFT]
    speedy = offset[K_DOWN]

    now = pygame.time.get_ticks()
    if offset[K_UP]:
        if now - piece_last_rotate_time > PIECE_ROTATE_FREQ:
            curr_piece['index'] = (curr_piece['index'] + 1) % len(curr_piece['shape'])
            if not validate_pos(board, curr_piece):
                curr_piece['index'] = (curr_piece['index'] - 1) % len(curr_piece['shape'])
            piece_last_rotate_time = now

    if now - piece_last_move > PIECE_MOVE_FREQ:
        if speedx and validate_pos(board, curr_piece, x_off=speedx):
            curr_piece['x'] += speedx
        if speedy and validate_pos(board, curr_piece, y_off=speedy):
            curr_piece['y'] += speedy
        piece_last_move = now

    now = pygame.time.get_ticks()
    if now - piece_last_down_time > PIECE_DOWN_FREQ:
        if validate_pos(board, curr_piece, y_off=1):
            curr_piece['y'] += 1
        else:
            addToBoard(board, curr_piece)
            remove_competed_lines(board, curr_piece['y'])
            curr_piece = None
        piece_last_down_time = now

    screen.fill(BLACK)

    draw_board(board)
    if curr_piece != None:
        draw_piece(screen, curr_piece, curr_piece['x'], curr_piece['y'])
    else:
        curr_piece = new_piece()
        piece_last_down_time = pygame.time.get_ticks()
    
    pygame.display.flip()
    clock.tick(FPS)
