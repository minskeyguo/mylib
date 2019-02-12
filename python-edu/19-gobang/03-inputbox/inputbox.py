#!/usr/bin/python3
# -*- coding:utf-8 -*-

import string
import pygame
from pygame import *

BLACK = (0, 0, 0)
DARK_GRAY = (80, 80, 80)
GRAY = (120, 120, 120)
LIGHT_GRAY = (160, 160, 160)
WHITE = (255,255,255)
GREEN = (0, 255, 0)

pygame.init()
DEFAULT_FONT = pygame.font.SysFont(None, 24)

class Inputbox(object):
    def __init__(self, parent, **kwargs):
        self._parent = parent
        self._buffer = []
        self.__parse_properties(kwargs)
        self._rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.last_inputs = None
        self.text_image = None

    def __parse_properties(self, kwargs):
        properties = {
                "id": None,
                "fgcolor": BLACK,
                "bgcolor": LIGHT_GRAY,
                "font": DEFAULT_FONT,
                "active": False,
                "visable": True,
                "x": 0,
                "y": 0,
                "width": 200,
                "height": 30,
                "callback": None,
                }
        for prop in kwargs:
            if prop in properties:
                properties[prop] = kwargs[prop]
            else:
                raise ValueError(":".join(("Invalid properties", str(prop))))
        self.__dict__.update(properties)

    def __update(self):
        new = "".join(self._buffer)
        if new != self.last_inputs:
            self.last_inputs = new
            self.text_image = self.font.render(new, True, self.fgcolor, self.bgcolor)
            self.text_rect = self.text_image.get_rect()
            if self.text_rect.width > self._rect.width - 4:
                self.text_rect.width = self._rect.width -4
            if self.text_rect.height > self._rect.height - 4:
                self.text_rect.height = self._rect.height -4

    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            self.active = self._rect.collidepoint(event.pos)
        elif self.active and event.type == KEYDOWN:
            if event.key == K_BACKSPACE and len(self._buffer):
                self._buffer.pop()
            elif event.unicode in string.ascii_letters + string.digits + ".":
                self._buffer.append(event.unicode)
        self.__update()

    def draw(self):
        if not self.visable: return
        pygame.draw.rect(self._parent, self.bgcolor, self._rect)
        pygame.draw.rect(self._parent, GREEN, self._rect, 1)
        self._parent.blit(self.text_image, (self._rect.x + 2, self._rect.y + 2), self.text_rect)

    def getText(self):
        return self._buffer


if __name__ == '__main__':
    import sys
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    inputbox = Inputbox(screen, width=240, height=30)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            inputbox.handleEvent(event)

        screen.fill(BLACK)
        inputbox.draw()
        pygame.display.flip()

