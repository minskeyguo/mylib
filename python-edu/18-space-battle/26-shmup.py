#!/usr/bin/python3

#-*- coding:utf-8 -*-

import sys
import pygame
import random
from os import path
from pygame.locals import *

img_dir = "images"
snd_dir = "sound"

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (50, 50, 50)
WHITE = (255,255,255)


"""
add more lives to player
"""

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

        self.shield = 100

        self.shoot_delay = 200
        self.last_shoot = pygame.time.get_ticks()

        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):

        # after player dead, if there is more lives, hide a second
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = SCREEN_WIDTH // 2
            self.rect.bottom = SCREEN_HEIGHT - 10

        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.speedx = -5
        if keys[K_RIGHT]:
            self.speedx = 5
        if keys[K_SPACE]:
            self.shoot()

        self.rect.x += self.speedx

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            bullet = Bullet(self.rect.centerx, self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
            shoot_snd.play()
            self.last_shoot = now

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT + 200)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.orig_image = random.choice(meteor_images)
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

    # repeatedly rotation destroy image, use self.rot to save the accumulated
    # rot degrees, and rotate orignal image by accumulated degree
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 30:
            old_center = self.rect.center
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            self.image = pygame.transform.rotate(self.orig_image, self.rot)
            self.rect.center = old_center

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

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 80

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect.center = center


class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text = font.render(text, True, WHITE)
    rect = text.get_rect()
    rect.midtop = (x, y)
    surf.blit(text, rect)

def draw_shield_bar(surf,pt, x, y):
    if pt < 0:
        pt = 0
    WIDTH = 100
    HEIGHT = 10
    fill = (pt / 100) * WIDTH
    outline_rect = pygame.Rect(x, y, WIDTH, HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        rect = img.get_rect()
        rect.x = x + 30 * i
        rect.y = y
        surf.blit(img, rect)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plane Flight")

# Load all game graphics
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png")).convert()
player_img_mini = pygame.transform.scale(player_img, (25,19))
player_img_mini.set_colorkey(player_img_mini.get_at((0,0)))

bullet_img = pygame.image.load(path.join(img_dir, "laserRed16.png")).convert()

meteor_images = []
meteor_list = [ "meteorBrown_big1.png", "meteorBrown_big2.png", 
                "meteorBrown_med1.png", "meteorBrown_med3.png", 
                "meteorBrown_small1.png", "meteorBrown_small2.png", 
                "meteorBrown_tiny1.png", "meteorBrown_tiny2.png"]
for x in meteor_list:
    img = pygame.image.load(path.join(img_dir, x)).convert()
    meteor_images.append(img)


shoot_snd = pygame.mixer.Sound(path.join(snd_dir, "pew.wav"))
explode_sounds = []
for s in ['expl3.wav', 'expl6.wav']:
    snd = pygame.mixer.Sound(path.join(snd_dir, s))
    explode_sounds.append(snd)
bk_snd = pygame.mixer.music.load(path.join(snd_dir, "tgfcoder-FrozenJam-SeamlessLoop.ogg"))

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(img.get_at((0,0)))
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename_pl = 'sonicExplosion0{}.png'.format(i)
    img_pl = pygame.image.load(path.join(img_dir, filename_pl)).convert()
    img_pl.set_colorkey(img.get_at((0, 0)))
    explosion_anim['player'].append(img_pl)

powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

clock = pygame.time.Clock()

# scores of the player
play_scores = 0

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
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for m in hits: 
        player.shield -= m.radius // 2
        expl = Explosion(m.rect.center, 'sm')
        all_sprites.add(expl)

        newm = Mob()
        all_sprites.add(newm)
        mobs.add(newm)

        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)

            # reduce a life of this player
            player.hide()
            player.lives -= 1
            player.shield = 100

            # running = False

    # if both player and death_explosion don't belong to any group
    if player.lives == 0 and not death_explosion.alive():
        running = False

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        snd = random.choice(explode_sounds)
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        snd.play()
        
        # 7% chance to get a powerup
        if random.random() > 0.93:
            p = Pow(hit.rect.center)
            all_sprites.add(p)
            powerups.add(p)

        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

        # the smaller meteor is hit, the more scores is given
        play_scores += 50 - hit.radius

        
    # render this frame
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(play_scores), 18, SCREEN_WIDTH // 2, 10)
    draw_shield_bar(screen, player.shield, 5, 5)
    draw_lives(screen, SCREEN_WIDTH - 100, 5, player.lives, player_img_mini)

    # display this frame
    pygame.display.flip()

