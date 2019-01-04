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

plane_img1 = pygame.image.load("resources/image/plane_ok_1.png")
plane_img2 = pygame.image.load("resources/image/plane_ok_2.png")

bk_music.play(-1)

clock = pygame.time.Clock()
tick = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bk_img, (0,0))
    if tick % 30 < 15 :
        screen.blit(plane_img1, (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 //3))
    else:
        screen.blit(plane_img2, (SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 //3))
    tick += 1
    pygame.display.update()
    clock.tick(30)
