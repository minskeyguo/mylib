#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255,255)
WIDTH, HEIGHT = 640, 480



class Paddle:
    def __init__(self, width, height, color, xpos, ypos):
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.surface.Surface((width, height))
        self.surface.fill(color)
        self.pos = self.surface.get_rect().move((xpos, ypos))

    def get_pos(self):
        return self.pos

    def move(self, offset):
        x_off = offset[K_RIGHT] - offset[K_LEFT] 
        if x_off > 0 and self.pos.left + x_off <= WIDTH or x_off < 0 and self.pos.left + x_off >= 0:
            self.pos.left = self.pos.left + x_off


class Ball:
    def __init__(self, radius, color, speed):
        self.radius = radius
        self.speed = speed
        self.surface = pygame.surface.Surface((radius *2, radius * 2))
        pygame.draw.circle(self.surface, color, (radius, radius), 20)
        self.surface.set_colorkey(self.surface.get_at((0,0)), RLEACCEL)
        self.pos = self.surface.get_rect()

    def get_pos(self):
        return self.pos

    def move(self):
        self.pos = self.pos.move(self.speed)
        if self.pos.right > WIDTH or self.pos.left < 0:
            self.speed[0] = - self.speed[0]
        if self.pos.bottom > HEIGHT or self.pos.top < 0:
            self.speed[1] = - self.speed[1]

def rect_collision(r1, r2):
    if r1.right < r2.left or r1.left > r2.right:
        return False
    if r1.bottom < r2.top:
        return False;
    return True;


def main():
    offset = { K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball = Ball(20, RED, [5, 5])
    pad = Paddle(180, 20, BLUE, (WIDTH - 180) //2, HEIGHT - 20 * 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                offset[event.key] = 5
            elif event.type == KEYUP:
                offset[event.key] = 0

        ball.move()
        pad.move(offset)

        if rect_collision(ball.pos, pad.pos):
            ball.speed[1] = -ball.speed[1]

        screen.fill(WHITE)
        screen.blit(ball.surface, ball.get_pos())
        screen.blit(pad.surface, pad.get_pos())
        
        pygame.display.update()
        pygame.time.delay(30)

if __name__ == "__main__":
    main()
