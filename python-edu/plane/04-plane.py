#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import pygame
from pygame.locals import *


SCREEN_WIDTH, SCREEN_HEIGHT = 480, 700

offset = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}

class Plane(pygame.sprite.Sprite):
    __images = ["resources/image/plane_ok_1.png", "resources/image/plane_ok_2.png"]

    def __init__(self, pos=(0,0), speed=5):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for x in Plane.__images:
            img = pygame.image.load(x)
            self.images.append(img)

        self.rect = self.images[0].get_rect()
        self.rect.topleft = pos
        self.speed = speed
        self.bullets = pygame.sprite.Group()

    def move(self, offset):
        x_off = offset[K_RIGHT] - offset[K_LEFT]
        y_off = offset[K_DOWN] - offset[K_UP]
        self.rect = self.rect.move(x_off, y_off)
        
    def OneShot(self):
        bullet = Bullet(((self.rect.left + self.rect.right) // 2, self.rect.top), 5)
        self.bullets.add(bullet)
    

class Bullet(pygame.sprite.Sprite):
    __images = ["resources/image/bullet1.png", "resources/image/bullet2.png"]
    def __init__(self, pos=(0,0), speed=3):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for x in Bullet.__images:
            img = pygame.image.load(x)
            self.images.append(img)
        self.rect = self.images[0].get_rect()
        self.rect.topleft = pos
        self.speed = speed
        self.image = self.images[0]

    def move(self):
        pass

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Flight")

bk_img = pygame.image.load("resources/image/background.png")
bk_music = pygame.mixer.Sound("resources/music/game_music.ogg")

plane_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 //3]

bk_music.play(-1)

tick = 0
clock = pygame.time.Clock()



plane = Plane(plane_pos, 5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            offset[event.key] = 5
        elif event.type == KEYUP:
            offset[event.key] = 0
    

    screen.blit(bk_img, (0,0))
    plane.move(offset)

    if tick % 30 < 15:
        screen.blit(plane.images[0], plane.rect)
    else:
        screen.blit(plane.images[1], plane.rect)
    tick += 1

    # bullet frequency 
    if tick % 15 == 0:
        plane.OneShot()

    plane.bullets.update()
    plane.bullets.draw(screen)

    pygame.display.update()
    clock.tick(60)
