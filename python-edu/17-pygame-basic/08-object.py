#!/usr/bin/python3


import sys, pygame
from pygame.locals import *


class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(self.speed)
        if self.pos.right > width or self.pos.left < 0:
            self.speed[0] = -self.speed[0]
        if self.pos.bottom > height or self.pos.top < 0:
            self.speed[1] = -self.speed[1]


wsize = width, height = 1280,720

screen = pygame.display.set_mode(wsize)
player = pygame.image.load('resources/cat.png').convert()
# player.set_colorkey((255,255,255), RLEACCEL)

background = pygame.image.load('resources/bk.jpg').convert()
screen.blit(background, (0, 0))

objects = []
for x in range(1):
    s = [5, 5]
    o = GameObject(player, x*40, s)
    objects.append(o)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    for o in objects:
        screen.blit(background, o.pos, o.pos)

    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)

    pygame.display.update()
    # pygame.display.flip()

    pygame.time.delay(100)
