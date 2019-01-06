#!/usr/bin/python3

import pygame
from pygame.locals import *


pygame.init()


# pygame.display.set_mode()返回的Surface对象叫作显示Surface(display Surface)。
# 绘制到显示Surface对象上的任何内容,当调用pygame.display.update()函数的时候,
# 都会显示到窗口上. 窗口的边框、标题栏和按钮并不是Surface对象的一部分
# 内容绘制到一个Surface对象中, 在游戏循环的迭代中,一旦将一个Surface对象上的
# 所有内容都绘制到了显示Surface对象上(这叫作一帧
# (resolution, flags, color_depth)
surface = pygame.display.set_mode((400, 300)) # return pygame.Surface
# flags: FULLSCREEN, DOUBLEBUF, HWSURFACE, OPENGL, RESIZABLE, NOFARME
# surface = pygame.display.set_mode((400, 300), FULLSCREEN) # return pygame.Surface


pygame.display.set_caption("Hello") # set the title of the window


# without events, the program will exit soon
for event in pygame.event.get():
    # QUIT etc, defined in pygame.locals
    if event.type == QUIT:    
        pygame.quit()
        sys.exit()
pygame.display.update()  # render surface into screen

"""
# event loop: handling event, update game state(variables), rendering graphics
while True:
    for event in pygame.event.get():

        # QUIT etc, defined in pygame.locals
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()
    pygame.display.update()  # render surface into screen

"""
