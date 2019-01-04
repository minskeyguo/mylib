#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import random
import pygame
from pygame.locals import *


SCREEN_WIDTH, SCREEN_HEIGHT = 480, 700

offset = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}

class Plane(pygame.sprite.Sprite):
    __images = ["resources/image/plane_ok_1.png", "resources/image/plane_ok_2.png"]
    __images_down = ["resources/image/plane_destroy_1.png",
        "resources/image/plane_destroy_2.png",
        "resources/image/plane_destroy_3.png",
        "resources/image/plane_destroy_4.png"]

    def __init__(self, pos=(0,0), speed=5):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for x in Plane.__images:
            img = pygame.image.load(x)
            self.images.append(img)

        self.images_down = []
        for x in Plane.__images_down:
            img = pygame.image.load(x)
            self.images_down.append(img)

        self.rect = self.images[0].get_rect()
        self.rect.topleft = pos
        self.speed = speed
        self.bullets = pygame.sprite.Group()
        self.crash = False
        self.down_index = 0

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
        self.image = self.images[1]

    def move(self):
        pass

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    __images = ["resources/image/enemy1.png"]
    __images_down = ["resources/image/enemy1_down1.png",
                    "resources/image/enemy1_down2.png",
                    "resources/image/enemy1_down3.png",
                    "resources/image/enemy1_down4.png"]
    def __init__(self, pos=(SCREEN_WIDTH // 2, 0), speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for x in Enemy.__images: 
            img = pygame.image.load(x)
            self.images.append(img)

        self.rect = self.images[0].get_rect()
        self.rect.topleft = pos
        self.speed = speed
        self.image = self.images[0]

        self.down_images = []
        for x in Enemy.__images_down:
            img = pygame.image.load(x)
            self.down_images.append(img)
        self.down_index = 0

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
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
enemy_group = pygame.sprite.Group()
enemy_down = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            offset[event.key] = 5
        elif event.type == KEYUP:
            offset[event.key] = 0

    tick += 1

    screen.blit(bk_img, (0,0))
    plane.move(offset)

    if plane.crash:
        if tick % 10 == 0:
            if plane.down_index < 3:
                plane.down_index += 1
            elif plane.down_index == 3:
                print("Game Over")
        screen.blit(plane.images_down[plane.down_index], plane.rect)
    else:
        if tick % 30 < 15:
            screen.blit(plane.images[0], plane.rect)
        else:
            screen.blit(plane.images[1], plane.rect)

        # bullet frequency 
        if tick % 15 == 0:
            plane.OneShot()

        plane.bullets.update()
        plane.bullets.draw(screen)

        e = pygame.sprite.spritecollideany(plane, enemy_group)
        if e != None:
            enemy_group.remove(e)
            enemy_down.add(e)
            plane.crash = 1

        d=pygame.sprite.groupcollide(enemy_group, plane.bullets, True, True)
        enemy_down.add(d)

        # bomb effect
        for e in enemy_down:
            image = e.down_images[e.down_index]
            screen.blit(image, e.rect)
            if tick % 10 == 0:
                if e.down_index < 3:
                    e.down_index += 1
                elif e.down_index == 3:
                    enemy_down.remove(e)

        if tick % 20 == 0:
            e = Enemy((random.randint(0, SCREEN_WIDTH), 0), 2)
            enemy_group.add(e)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
    clock.tick(60)
