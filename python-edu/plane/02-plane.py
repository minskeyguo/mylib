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
plane_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 //3]

bk_music.play(-1)

tick = 0
clock = pygame.time.Clock()

offset = { K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            offset[event.key] = 5
        elif event.type == KEYUP:
            offset[event.key] = 0
    
    x_off = offset[K_RIGHT] - offset[K_LEFT]
    y_off = offset[K_DOWN] - offset[K_UP]
    plane_pos[0] += x_off 
    plane_pos[1] += y_off

    screen.blit(bk_img, (0,0))
    if tick % 16 < 8:
        screen.blit(plane_img1, plane_pos)
    else:
        screen.blit(plane_img2, plane_pos)
    tick += 1

    pygame.display.update()
    clock.tick(30)
