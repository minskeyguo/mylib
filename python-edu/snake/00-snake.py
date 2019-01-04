#!/usr/bin/python3

import pygame
import time
from pygame.locals import *

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 32
        self.direction = 0

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed


SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.image = None
        self.player = Player()

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.running = True
        self.image = pygame.image.load("snake.png").convert()

    def on_even(self, event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        self.player.update()
        time.sleep(100.0 / 1000.0)

    def on_render(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.image, (self.player.x, self.player.y))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while self.running:
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()

            if keys[K_LEFT]:
                self.player.moveLeft()

            if keys[K_UP]:
                self.player.moveUp()

            if keys[K_DOWN]:
                self.player.moveDown()

            if keys[K_ESCAPE]:
                self.running = False

            self.on_loop()
            self.on_render()

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()






