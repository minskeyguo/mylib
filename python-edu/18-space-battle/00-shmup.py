#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import pygame
from pygame.locals import *


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 700

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speedx = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.speedx = -5
        elif keys[K_RIGHT]:
            self.speedx = 5
        else:
            self.speedx = 0
        self.rect.x += self.speedx

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Flight")

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(BLACK)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()


"""
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                player.speedx = -8
            if event.key = K_RIGHT:
                player.speedx = 8
"""
