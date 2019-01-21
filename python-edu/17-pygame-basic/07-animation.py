#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

FPS=30 # frames per second
WHITE = (255, 255, 255)

pygame.init()
fpsClock = pygame.time.Clock()

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')


Img = pygame.image.load('resources/cat.png')
x = 10
y = 10

direction = 'right'

while True: # the main game loop
    surface.fill(WHITE)

    if direction == 'right':
        x += 5
        if x == 280:
            direction = 'down'
    elif direction == 'down':
        y += 5
        if y == 220:
            direction = 'left'
    elif direction == 'left':
        x -= 5
        if x == 10:
            direction = 'up'
    elif direction == 'up':
        y -= 5
        if y == 10:
            direction = 'right'

    surface.blit(Img, (x, y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)

"""
FPS=30 # frames per second
WHITE = (255, 255, 255)

W, H = 640, 480

class GameObject:
    def __init__(self, image, speed, direction, winsize):
        self.image = image
        self.winsize = winsize
        self.speed = speed
        self.direction = direction
        self.pos = image.get_rect().move(0, 0)

    def move(self):
        x, y = 0, 0
        if self.direction == "left":
            x = -self.speed
            if self.pos.left <= 0:
                self.direction = "up"
        elif self.direction == "right":
            x = self.speed
            if self.pos.right >= self.winsize[0]:
                self.direction = "down"
        elif self.direction == "up":
            y = -self.speed
            if self.pos.top <= 0:
                self.direction = "right"
        else:
            y = self.speed
            if self.pos.bottom > self.winsize[1]:
                self.direction = "left"
        self.pos = self.pos.move(x,y)



if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    surface = pygame.display.set_mode((W,H), 0, 32)
    pygame.display.set_caption('Animation')

    img = pygame.image.load('resources/cat.png')
    obj = GameObject(img, 5, "right", (W, H))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        surface.fill(WHITE)
        obj.move()
        surface.blit(obj.image, obj.pos)
        clock.tick(FPS)
        pygame.display.update()

"""

