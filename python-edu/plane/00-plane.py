#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import pygame
from pygame.locals import *


SCREEN_WIDTH, SCREEN_HEIGHT = 480, 700

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Flight")

bk_img = pygame.image.load("resources/image/background.png")
bk_music = pygame.mixer.Sound("resources/music/game_music.ogg")

# plane_img = pygame.image.load("resources/image/plane.png")

bk_music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bk_img, (0,0)) 
    pygame.display.update()
