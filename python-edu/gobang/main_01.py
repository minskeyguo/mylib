#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame, sys
from pygame import *
from enum import Enum
from gobang_01 import *

# background.jpg is 1024 x 768
SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 768

# Gobang is 15 x 15 lines
BOARD_LINES = 15

# chessboard.jpg is 535, 535, Use inkscape to open the image. 
# we can see that chessboard (0,0) is pixel(22,22), (14,14) is pixel(518,518)
BOARD_WIDTH, BOARD_HEIGHT = 535, 535

GRID_SIZE = (518 - 22) // (BOARD_LINES - 1)
PIECE_SIZE = 32

X_OFFSET, Y_OFFSET = 100, 100

class Application(object):
    def __init__(self, gobang):
        self.game = gobang
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.backgroud_img = pygame.image.load("background.jpg").convert()

        self.board_img = pygame.image.load("chessboard.png").convert()
        self.board_rect = self.board_img.get_rect()
        self.board_rect.topleft= (X_OFFSET, Y_OFFSET)

        self.piece_black = pygame.image.load("blackpiece.png").convert()
        self.piece_black.set_colorkey(self.piece_black.get_at((0,0)))
        self.piece_black_mini = pygame.transform.scale(self.piece_black, (24,24))
        self.piece_white = pygame.image.load("whitepiece.png").convert()
        self.piece_white.set_colorkey(self.piece_white.get_at((0,0)))
        self.piece_white_mini = pygame.transform.scale(self.piece_white, (24, 24))

        self.curr_move_x = None
        self.curr_move_y = None
        self.curr_move_color = GRID_STATE_BLACK
        
        self.winner = GRID_STATE_EMPTY

    def grid_2_pixel(self, i, j):
        # chessboard grid(0,0) is pixel(22,22), (14,14) is pixel(518,518)
        return (22 + GRID_SIZE * j - PIECE_SIZE // 2 + X_OFFSET, 
               22 + GRID_SIZE * i - PIECE_SIZE //2 + Y_OFFSET)

    def pixel_2_grid(self, x, y):
        i = (y - Y_OFFSET - 22 + GRID_SIZE // 4) // GRID_SIZE
        j = (x - X_OFFSET - 22 + GRID_SIZE // 4) // GRID_SIZE
        if i < 0 or i>= BOARD_LINES or j < 0 or j>=BOARD_LINES:
            i, j = None, None
        return i,j

    def one_move_begin(self):
        btn = pygame.mouse.get_pressed()
        if btn[0]:
            x, y = pygame.mouse.get_pos()
            self.curr_move_x, self.curr_move_y = x, y

    def one_move_inprocess(self):
        if self.curr_move_x is not None:
            x, y = pygame.mouse.get_pos()
            self.curr_move_x, self.curr_move_y = x, y

    def one_move_end(self):
        if self.curr_move_x is None:
            return
        self.curr_move_x, self.curr_move_y = None, None
        x, y = pygame.mouse.get_pos()
        i, j = self.pixel_2_grid(x, y)
        if i == None or j == None:
            return
        ok = self.game.set_state(i, j, self.curr_move_color)
        # print_states(self.game)
        if ok:
            if game.find_connected_five(i, j):
                self.winner = self.curr_move_color
                
            if self.curr_move_color == GRID_STATE_WHITE:
                self.curr_move_color = GRID_STATE_BLACK
            else:
                self.curr_move_color = GRID_STATE_WHITE

    def draw_pieces(self):
        for i in range(BOARD_LINES):
            for j in range(BOARD_LINES):
                x, y = self.grid_2_pixel(i, j)
                color = self.game.get_state(i, j)
                if color == GRID_STATE_BLACK:
                    self.screen.blit(self.piece_black, (x,y))
                elif color == GRID_STATE_WHITE:
                    self.screen.blit(self.piece_white, (x,y))
                else:
                    pass
        if self.curr_move_x is not None:
            if self.curr_move_color == GRID_STATE_BLACK:
                self.screen.blit(self.piece_black_mini, (self.curr_move_x - PIECE_SIZE // 2, self.curr_move_y - PIECE_SIZE // 2 ))
            else:
                self.screen.blit(self.piece_white_mini, (self.curr_move_x - PIECE_SIZE // 2, self.curr_move_y - PIECE_SIZE // 2 ))

    def draw_text(self, message, x, y, size):
        font = pygame.font.Font(None, size)
        text = font.render(message,True, (255,0,0))
        self.screen.blit(text, (x, y))


    # draw a frame
    def draw(self):
        self.screen.blit(self.backgroud_img, (0,0))
        self.screen.blit(self.board_img, self.board_rect)
        self.draw_pieces()
        if self.winner != GRID_STATE_EMPTY:
            s =  "White Win" if self.winner == GRID_STATE_WHITE  else "Black Win"
            self.draw_text(s, X_OFFSET + BOARD_WIDTH // 2, Y_OFFSET + BOARD_HEIGHT // 2, 64)
        pygame.display.flip()


if __name__ == '__main__':
    game = Gobang(GRID_STATE_BLACK)
    app = Application(game)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                app.one_move_begin()
            elif event.type == MOUSEMOTION:
                app.one_move_inprocess()
            elif event.type == MOUSEBUTTONUP:
                app.one_move_end()

        app.draw()

