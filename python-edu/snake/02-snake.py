#!/usr/bin/python3

import pygame
import time
from pygame.locals import *

class Apple:
    def __init__(self, x, y):
        self.step = 44
        self.x = x * self.step
        self.y = y * self.step
    
    def draw(self, surf, image):
        surf.blit(image, (self.x, self.y))

class Player:
    def __init__(self, length):
        self.x = []
        self.y = []
        self.step = 44
        self.direction = 0

        self.updateCountMax = 2
        self.updateCount = 0

        self.length = length
        for i in range(0, length):
            self.x.append(0)
            self.y.append(0)

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3

    def update(self):
        self.updateCount += 1
        if self.updateCount > self.updateCountMax:

            for i in range(self.length -1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.updateCount = 0

    def draw(self, screen, image):
        for i in range(0, self.length):
            screen.blit(image, (self.x[i], self.y[i]))

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
class App:
    def __init__(self):
        self.running = True
        self.screen = None
        self.player_image = None
        self.apple_image = None
        self.player = Player(10)
        self.apple = Apple(5,5)

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.running = True
        self.player_image = pygame.image.load("snake.png").convert()
        self.apple_image = pygame.image.load("apple.png").convert()

    def on_even(self, event):
        if event.type == QUIT:
            self.running = False

    def on_loop(self):
        self.player.update()


    def on_render(self):
        self.screen.fill((0,0,0))
        self.player.draw(self.screen, self.player_image)
        self.apple.draw(self.screen, self.apple_image)
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

            time.sleep(100.0 / 1000.0)
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()






