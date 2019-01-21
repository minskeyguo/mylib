#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame, sys
from pygame import *

# Gobang is 15 x 15 lines
BOARD_LINES = 15

GRID_STATE_BLACK = -1
GRID_STATE_EMPTY = 0
GRID_STATE_WHITE = 1

'''
    [(50, (0, 1, 1, 0, 0)),
    (50, (0, 0, 1, 1, 0)),
    (200, (1, 1, 0, 1, 0)),
    (500, (0, 0, 1, 1, 1)),
    (500, (1, 1, 1, 0, 0)),
    (5000, (0, 1, 1, 1, 0)),
    (5000, (0, 1, 0, 1, 1, 0)),
    (5000, (0, 1, 1, 0, 1, 0)),
    (5000, (1, 1, 1, 0, 1)),
    (5000, (1, 1, 0, 1, 1)),
    (5000, (1, 0, 1, 1, 1)),
    (5000, (1, 1, 1, 1, 0)),
    (5000, (0, 1, 1, 1, 1)),
    (50000, (0, 1, 1, 1, 1, 0)),
    (99999999, (1, 1, 1, 1, 1))]
'''
class Gobang(object):
    def __init__(self, first_color):
        self.chessMap = [[GRID_STATE_EMPTY for i in range(BOARD_LINES)] for j in range(BOARD_LINES)]
        self.curr_turn = first_color
        self.history_move = []

    def get_state(self, row, colume):
        return self.chessMap[row][colume]

    def set_state(self, row, colume, color):
        if self.chessMap[row][colume] == GRID_STATE_EMPTY and self.curr_turn == color:
            self.chessMap[row][colume] = color
            self.history_move.append((row, colume, color))
            self.curr_turn = -color
            return True
        return False

    def withdraw_state(self, color):
        if len(self.history_move) != 0 and self.curr_turn == -color:
            row, colume, color = self.history_move.pop()
            self.chessMap[row][colume] = GRID_STATE_EMPTY
            self.curr_turn = color
            return True
        return False


    def count_connected_pieces(self, i, j, xstep, ystep, color):
        '''
        count the connected chess pieces to postion (i,j) in 8 directions
            xstep: step in x-asix direction (-1, 0, 1)
            ystep: step in y-asix direction (-1, 0, 1)
        '''
        count = 0
        for k in range(1,5):
            m = i + ystep * k
            n = j + xstep * k
            if m < 0 or m >= BOARD_LINES:
                break
            if n < 0 or n >= BOARD_LINES:
                break
            if self.chessMap[m][n] == color:
                count += 1
            else:
                break
        return count

    def find_connected_five(self, row, colume):
        '''
        count the connected chess pieces to postion (row,colume) in 8 directions
        return True, if found 5; otherwise, return false
        '''
        directions = [ ((-1, 0), (1, 0)), # x-direction
                 ((0, -1), (0, 1)), # y-direction
                 ((-1, 1), (1, -1)), # topleft--bottomright
                 ((-1, -1), (1, 1)) ] # topright -- bottomleft

        color = self.chessMap[row][colume]

        for step in directions:
            count = 1
            for (xstep, ystep) in step:
                count += self.count_connected_pieces(row, colume, xstep, ystep, color)
                if count >= 5:
                    return True
        return False


class Player():
    def __init__(self, color, inType):
        player_type = { "console": self.console_next_move, 
                    "network": self.net_next_move,
                    "robot": self.robot_next_move}
        self.color = color
        self.one_move = player_type[inType]

    def console_next_move(self):
        if self.color == GRID_STATE_BLACK:
            prompt = "Black's turn (row, volume), 'q' to quit: "
        else:
            prompt = "White's turn (row, volume), 'q' to quit: "

        quit = False
        row, col = None, None
        while True:
            try:
                s = input(prompt)
                row, col = s.replace(',', ' ').split()
                row = int(row)
                col= int(col)
                break
            except:
                if s == 'q': quit=True; break
        return row, col, self.color, quit

    def net_next_move(self):
        pass

    def robot_next_move(self):
        pass


#===================================================================
# The following is to test if class Gobang works
#
def print_states(go):
    char = {GRID_STATE_EMPTY:"-", GRID_STATE_BLACK:"X", GRID_STATE_WHITE:"O"}
    s = "   "
    for j in range(BOARD_LINES):
        s += "{:3d}".format(j)
    print(s)

    for i in range(BOARD_LINES):
        s = "{:5d}".format(i)
        for j in range(BOARD_LINES):
            s += "{:3s}".format(char[go.get_state(i, j)])
        print(s)


if __name__ == "__main__":
    go = Gobang(GRID_STATE_BLACK)
    player1 = Player(GRID_STATE_BLACK, "console")
    player2 = Player(GRID_STATE_WHITE, "console")

    while True:
        for player in (player1, player2):
            print_states(go)
            i, j, color, quit = player.one_move()
            if quit: sys.exit()
            go.set_state(i, j, color)
            
            if go.find_connected_five(i, j):
                print("%d win !!!" %player.color)
                sys.exit()

