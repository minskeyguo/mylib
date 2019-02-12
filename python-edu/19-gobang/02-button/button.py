#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame
from pygame import *

BLACK = (0, 0, 0)
DARK_GRAY = (80, 80, 80)
GRAY = (120, 120, 120)
LIGHT_GRAY = (160, 160, 160)
WHITE = (255,255,255)

pygame.init()
DEFAULT_FONT = pygame.font.SysFont(None, 24)

def trace(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper

class Button(object):
    def __init__(self, parent, **kwargs):
        self._mouseDown = False
        self._mouseOver = False
        self._lastMouseDownOverButton = False
        self._parent = parent
        self.__parse_properies(kwargs)

        self._rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.__setImage()

    def __parse_properies(self, kwargs):
        properties = {
            "visable": True,
            "caption": '', 
            "callback": None,
            "x": 0,
            "y": 0,
            "width": 50,
            "height": 25,
            "bgcolor": LIGHT_GRAY, 
            "fgcolor": BLACK, 
            "font" : DEFAULT_FONT, 
            "upImage": None, 
            "downImage": None, 
            "hiImage": None
          }
        for prop in kwargs:
            if prop in properties:
                properties[prop] = kwargs[prop]
        self.__dict__.update(properties)

    def __setImage(self):
        if self.upImage is None:
            self.upImage = pygame.Surface(self._rect.size)
            self.downImage = pygame.Surface(self._rect.size)
            self.hiImage = pygame.Surface(self._rect.size)
            self.drawButton()
            return

        if self.downImage is None:
            self.downImage = self.upImage
        if self.hiImage is None:
            self.hiImage = self.upImage
        if type(self.upImage) == str:
            self.upImage == pygame.image.load(self.upImage)
        if type(self.downImage) == str:
            self.downImage == pygame.image.load(self.downImage)
        if type(self.hiImage) == str:
            self.hiImage == pygame.image.load(self.hiImage)

        self._rect = self.upImage.get_rect().move(self._rect.left, self._rect.top)

    def mouseDown(self, event):
        pass
    def mouseUp(self, event):
        pass
    def mouseEnter(self, event):
        pass
    def mouseExit(self, event):
        pass
    def mouseMove(self, event):
        pass
    def mouseClick(self, event):
        if self.callback is not None:
            self.callback()

    def draw(self):
        if not self.visable:
            return
        if self._mouseDown :
            self._parent.blit(self.downImage, self._rect)
        elif self._mouseOver:
            self._parent.blit(self.hiImage, self._rect)
        else:
            self._parent.blit(self.upImage, self._rect)

    def drawButton(self):
        self.upImage.fill(self.bgcolor)
        self.downImage.fill(self.bgcolor)
        self.hiImage.fill(self.bgcolor)

        w = self._rect.width
        h = self._rect.height
        text = self.font.render(self.caption, True, self.fgcolor, self.bgcolor)
        rect = text.get_rect()
        rect.center = (w //2, h //2)

        self.upImage.blit(text, rect)
        self.downImage.blit(text, (rect.x +1, rect.y + 1, rect.width, rect.height))

        pygame.draw.rect(self.upImage, BLACK, pygame.Rect(0, 0, w, h), 1)
        pygame.draw.line(self.upImage, WHITE, (1, 1), (w - 2, 1))
        pygame.draw.line(self.upImage, WHITE, (1, 1), (1, h - 2))
        pygame.draw.line(self.upImage, DARK_GRAY, (1, h - 1), (w - 1, h - 1))
        pygame.draw.line(self.upImage, DARK_GRAY, (w - 1, 1), (w - 1, h - 1))
        pygame.draw.line(self.upImage, GRAY, (2, h - 2), (w - 2, h - 2))
        pygame.draw.line(self.upImage, GRAY, (w - 2, 2), (w - 2, h - 2))

        pygame.draw.rect(self.downImage, BLACK, pygame.Rect(0, 0, w, h), 1)
        pygame.draw.line(self.downImage, DARK_GRAY, (1, 1), (w - 2, 1))
        pygame.draw.line(self.downImage, DARK_GRAY, (1, 1), (1, h - 2))
        pygame.draw.line(self.downImage, WHITE, (1, h - 1), (w - 1, h - 1))
        pygame.draw.line(self.downImage, WHITE, (w - 1, 1), (w - 1, h - 1))
        pygame.draw.line(self.downImage, GRAY, (2, h - 3), (2, 2))
        pygame.draw.line(self.downImage, GRAY, (2, 2), (w - 3, 2))

        self.hiImage = self.upImage

    def handleEvent(self, event):
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN) or not self.visable:
            return

        if self._rect.collidepoint(event.pos):
            if self._mouseOver == False:
                self._mouseOver = True
                self.mouseEnter(event)
            if event.type == MOUSEMOTION:
                self.mouseMove(event)
            elif event.type == MOUSEBUTTONDOWN:
                self._mouseDown = True
                self.mouseDown(event)
                self._lastMouseDownOverButton = True
            elif event.type == MOUSEBUTTONUP:
                self._mouseDown = False
                self.mouseUp(event)
                if self._lastMouseDownOverButton:
                    self.mouseClick(event)
                    self._lastMouseDownOverButton = False
        elif self._mouseOver:
            self._mouseOver = False
            self._lastMouseDownOverButton = False
            self.mouseExit(event)





if __name__ == '__main__':
    import sys
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    button = Button(screen, caption="Start", width=120, height=80)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            button.handleEvent(event)

        screen.fill(BLACK)
        button.draw()
        pygame.display.flip()

