#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame, sys
from pygame import *
from enum import Enum
from gobang_01 import *

import button, inputbox


FPS = 60

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

GAME_STATE_INIT = 0
GAME_STATE_START = 1
GAME_STATE_END = 2
GAME_STATE_SERVER = 3
GAME_STATE_CLIENT = 3

def game_start():
    app.game_state = GAME_STATE_START

def start_server():
    app.game_state = GAME_STATE_SERVER

def connect_to_server():
    app.game_state = GAME_STATE_CLIENT
    app.show_inputbox()

class Application(object):
    def __init__(self, gobang):
        game_state = GAME_STATE_INIT
        self.game = gobang
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        self.backgroud_img = pygame.image.load("../images/background.jpg").convert()

        self.board_img = pygame.image.load("../images/chessboard.png").convert()
        self.board_rect = self.board_img.get_rect()
        self.board_rect.topleft= (X_OFFSET, Y_OFFSET)

        self.piece_black = pygame.image.load("../images/blackpiece.png").convert()
        self.piece_black.set_colorkey(self.piece_black.get_at((0,0)))
        self.piece_black_mini = pygame.transform.scale(self.piece_black, (24,24))
        self.piece_white = pygame.image.load("../images/whitepiece.png").convert()
        self.piece_white.set_colorkey(self.piece_white.get_at((0,0)))
        self.piece_white_mini = pygame.transform.scale(self.piece_white, (24, 24))

        self.curr_move_x = None
        self.curr_move_y = None
        self.curr_move_color = GRID_STATE_BLACK
        
        self.winner = GRID_STATE_EMPTY

        self.start_button = button.Button(self.screen, callback=game_start, caption="Start Local Game", x=680, y=120, width=200, height=60)
        self.server_button = button.Button(self.screen, callback=start_server, caption="Start Game As Server", x=680, y=240, width=200, height=60)
        self.conn_button = button.Button(self.screen, callback=connect_to_server, caption="Connect to Game Server", x=680, y=360, width=200, height=60)
        self.conn_inputbox = None

        self.game_state = GAME_STATE_INIT

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
        self.start_button.draw()
        self.server_button.draw()
        self.conn_button.draw()
        if self.conn_inputbox is not None:
            self.conn_inputbox.draw()

        if self.winner != GRID_STATE_EMPTY:
            s =  "White Win" if self.winner == GRID_STATE_WHITE  else "Black Win"
            self.draw_text(s, X_OFFSET + BOARD_WIDTH // 2, Y_OFFSET + BOARD_HEIGHT // 2, 64)
            self.game_state = GAME_STATE_END
        pygame.display.flip()

    def handleEvent(self, event):
        if self.game_state == GAME_STATE_START:
            if event.type == MOUSEBUTTONDOWN:
                self.one_move_begin()
            elif event.type == MOUSEMOTION:
                self.one_move_inprocess()
            elif event.type == MOUSEBUTTONUP:
                self.one_move_end()
            return
        if self.game_state == GAME_STATE_INIT:
            self.start_button.handleEvent(event)
        if self.game_state == GAME_STATE_INIT:
            self.server_button.handleEvent(event)
        if self.game_state == GAME_STATE_INIT:
            self.conn_button.handleEvent(event)
        if self.game_state == GAME_STATE_CLIENT:
            self.conn_inputbox.handleEvent(event)

    def show_inputbox(self):
        self.conn_inputbox = inputbox.Inputbox(app.screen, active=True, x=690, y=430, width=120, height=40)

if __name__ == '__main__':
    clock = pygame.time.Clock()
    game = Gobang(GRID_STATE_BLACK)
    app = Application(game)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        app.handleEvent(event)
        app.draw()
        clock.tick(FPS)

