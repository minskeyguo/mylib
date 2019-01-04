#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255,255)

WIDTH, HEIGHT = 640, 480


class Brick:
    COLORS = { 1:(250, 250, 0), 2:(120, 120, 0), 3:(60, 60,0) }
    def __init__(self, width, height, hits, xpos, ypos):
        self.width = width
        self.height = height
        self.color = Brick.COLORS[hits]
        self.hits = hits
        self.surface = pygame.surface.Surface((width, height))
        pygame.draw.rect(self.surface, self.color, (0, 0, width, height))
        pygame.draw.rect(self.surface, WHITE, (0, 0, width, height), 2)
        self.pos = self.surface.get_rect().move((xpos, ypos))

    def hit(self):
        if self.hits > 1:
            self.hits -= 1
            self.color = Brick.COLORS[self.hits]
            pygame.draw.rect(self.surface, self.color, (3, 3, self.width-3, self.height-3))
            return False
        else:
            return True


class Paddle:
    def __init__(self, width, height, color, xpos, ypos):
        self.width = width
        self.height = height
        self.color = color
        self.surface = pygame.surface.Surface((width, height))
        self.surface.fill(color)
        self.pos = self.surface.get_rect().move((xpos, ypos))
        self.ball = None
        self.offset = { K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}

    def get_pos(self):
        return self.pos

    def set_ball(self, ball):
        self.ball = ball
        if ball is not None:
            pos = self.pos
            ball.pos.topleft = ((pos.left + pos.right)//2, pos.top - ball.radius * 2)
            ball.hit_bottom = False
            ball.speed = [5, -5]

    def update(self):
        x_off = self.offset[K_RIGHT] - self.offset[K_LEFT] 
        if x_off > 0 and self.pos.left + x_off <= WIDTH or x_off < 0 and self.pos.left + x_off >= 0:
            self.pos.left = self.pos.left + x_off
            if self.ball is not None:
                self.ball.move(x_off)

class Ball:
    def __init__(self, radius, color, speed):
        self.radius = radius
        self.speed = speed
        self.surface = pygame.surface.Surface((radius *2, radius * 2))
        pygame.draw.circle(self.surface, color, (radius, radius), radius)
        self.surface.set_colorkey(self.surface.get_at((0,0)), RLEACCEL)
        self.pos = self.surface.get_rect()
        self.hit_bottom = False

    def get_pos(self):
        return self.pos

    def update(self):
        self.pos = self.pos.move(self.speed)
        if self.pos.right > WIDTH or self.pos.left < 0:
            self.speed[0] = - self.speed[0]
        if self.pos.top < 0:
            self.speed[1] = - self.speed[1]
        if self.pos.bottom > HEIGHT:
            self.hit_bottom = True

    def move(self, x_off):
        self.pos = self.pos.update(x_off, 0)

def rect_collision(r1, r2):
    if r1.right < r2.left or r1.left > r2.right:
        return False
    if r1.bottom < r2.top:
        return False;
    return True;

def circle_rect_collision(c, r):
    (x, y) = c.pos.center
    if x >= r.left and x <= r.right and y - c.radius <= r.bottom and y + c.radius >= r.top:
        return True
    return False

font_name = pygame.font.match_font("arial")
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text = font.render(text, True, RED)
    rect = text.get_rect()
    rect.center = (x, y)
    surf.blit(text, rect)


GAME_STATE = ("READY", "START", "ROUND_OVER", "GAME_OVER")

def main():

    lives = 3

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    font = pygame.font.Font(None, 64)


    ball = Ball(15, RED, [5, 5])
    ball.pos.center = (WIDTH // 2, HEIGHT // 2)

    pad = Paddle(180, 20, (0,0,0), (WIDTH - 180) //2, HEIGHT - 20 * 2)
    pad.set_ball(ball)

    bricks = []
    for x in range (0, WIDTH, 80):
        for i in range(1, 4):
            b = Brick(80, 40, 4 - i, x, 40 * i)
            bricks.append(b)

    screen.fill(WHITE)
    screen.blit(ball.surface, ball.get_pos())
    screen.blit(pad.surface, pad.get_pos())
    for b in bricks:
        screen.blit(b.surface, b.pos)

    game_state = "READY"

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                pad.offset[event.key] = 8
            elif event.type == KEYUP:
                pad.offset[event.key] = 0

        if game_state == "READY":

            draw_text(screen, "Press SPACE key to start", 48, WIDTH // 2, HEIGHT // 2)
            draw_text(screen, "Lives={}".format(lives), 48, WIDTH // 2, HEIGHT // 2 - 50)
            keys = pygame.key.get_pressed()
            if keys[K_SPACE]:
                pad.set_ball(None)
                game_state = "START"

        elif game_state == "START":
            pad.update()
            ball.update()

            if ball.hit_bottom:
                game_state = "ROUND_OVER"

            if rect_collision(ball.pos, pad.pos):
                ball.speed[1] = -ball.speed[1]

            for brick in bricks:
                if circle_rect_collision(ball, brick.pos):
                    if brick.hit():
                        bricks.remove(brick)
                        del brick
                    ball.speed[1] = -ball.speed[1]
                    break
                      
            screen.fill(WHITE)
            screen.blit(ball.surface, ball.get_pos())
            screen.blit(pad.surface, pad.get_pos())
            for b in bricks:
                screen.blit(b.surface, b.pos)

        elif game_state == "GAME_OVER":
            draw_text(screen, "Game Over", 48, WIDTH // 2, HEIGHT // 2)

        elif game_state == "ROUND_OVER":
            lives -= 1
            if lives == 0:
                game_state = "GAME_OVER"
            else:
                pad.set_ball(ball)
                screen.fill(WHITE)
                screen.blit(ball.surface, ball.get_pos())
                screen.blit(pad.surface, pad.get_pos())
                for b in bricks:
                    screen.blit(b.surface, b.pos)
                game_state = "READY"


        pygame.display.update()
        pygame.time.delay(30)

if __name__ == "__main__":
    main()
