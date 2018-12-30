#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import pygame
import random
from os import path
from pygame.locals import *

img_dir = "images"

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (50, 50, 50)

FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # original player_img is 99 x 75
        self.image = pygame.transform.scale(player_img, (50,38))
        
        # colorkey
        self.image.set_colorkey(self.image.get_at((0,0)))

        self.rect = self.image.get_rect()

        # draw a circle on Mob image, we use circle to do collision detection
        self.radius = int(self.rect.width * 0.7 // 2) 
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

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

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.orig_image = meteor_img
        self.orig_image.set_colorkey(self.orig_image.get_at((0,0)))

        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect()

        # draw a circle on Mob image, we use circle to do collision detection
        self.radius = int(self.rect.width * 0.85 // 2) 
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)

        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 8)

        self.rot = 0   # accumulated rotation degree
        self.rot_speed = random.randrange(-5, 5)
        self.last_update = pygame.time.get_ticks()

    # repeatedly rotation destroy image, use self.rot to save the accumulated rot degrees,
    # and rotate orignal image by accumulated degree
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 30:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pygame.transform.rotate(self.orig_image, self.rot)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.rotate()
        if self.rect.top > SCREEN_HEIGHT + 10 or \
                self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Flight")

# Load all game graphics
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.shoot()
    
    # update position first
    all_sprites.update()

    # then, check collision. Use collide_circle() as collision detection func
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits: running = False

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # render this frame
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    # display this frame
    pygame.display.flip()


"""
After rotation, we need to recaculate image's Rect.

Rect's rotation is anchored at the topleft cornoer, but we need to keep the image's rect centered at the old location
"""
