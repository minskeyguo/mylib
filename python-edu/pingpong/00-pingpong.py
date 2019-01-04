#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255,255)
WIDTH, HEIGHT = 640, 480


class Ball:
    def __init__(self, radius, color, speed):
        self.radius = radius
        self.speed = speed
        self.surface = pygame.surface.Surface((radius *2, radius * 2))
        self.surface.set_colorkey(self.surface.get_at((0,0)), RLEACCEL)
        pygame.draw.circle(self.surface, color, (radius, radius), 20)
        self.pos = self.surface.get_rect()

    def get_pos(self):
        return self.pos

    def move(self):
        self.pos = self.pos.move(self.speed) 
        if self.pos.right > WIDTH or self.pos.left < 0:
            self.speed[0] = -self.speed[0]
        if self.pos.bottom > HEIGHT or self.pos.top < 0:
            self.speed[1] = -self.speed[1]

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball = Ball(20, RED, [5, 5])
#    gBall = Ball(20, GREEN, 4)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ball.move()

#        gBall.move()
        screen.fill(WHITE)
        screen.blit(ball.surface, ball.get_pos())
#        screen.blit(gBall.surface, gBall.get_pos())
        
        pygame.display.update()
        pygame.time.delay(30)

if __name__ == "__main__":
    main()
