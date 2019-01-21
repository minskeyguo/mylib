#!/usr/bin/python3

import sys
import pygame
from pygame.locals import *

BLACK=(0,0,0)
BLUE = (0, 0, 255)

pygame.init()

surface = pygame.display.set_mode((400, 300)) # return pygame.Surface

pygame.display.set_caption("Hello") # set the title of the window

font = pygame.font.Font(None, 32)

# pygame.key.set_repeat(10)

fs = font.render("mm: ", True, BLUE)

while True:
    for event in pygame.event.get():

        # QUIT etc, defined in pygame.locals
        if event.type == QUIT:    
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            print("KEYDOWN")
        elif event.type == KEYUP:
            print("keyup")
        elif event.type == MOUSEMOTION:
             mouse_x,mouse_y = event.pos
             print("mm: %d, %d" %(mouse_x, mouse_y))
#             fs = font.render("mm: " + str(mouse_x) + "," + str(mouse_y), True, BLUE)
        elif event.type == MOUSEBUTTONDOWN:
             mouse_x,mouse_y = event.pos
             print("md: %d, %d" %(mouse_x, mouse_y))
        elif event.type == MOUSEBUTTONUP:
             mouse_x,mouse_y = event.pos
             print("mu: %d, %d" %(mouse_x, mouse_y))

       # keys = pygame.key.get_pressed()
       # print(keys)

        surface.fill(BLACK)
        surface.blit(fs, (0, 0))

    pygame.display.update()  # render surface into screen



"""
pygame.event.EventType, its type is between NOEVENT and NUMEVENTS. All user defined
events can have the value of USEREVENT or higher.

QUIT             none
ACTIVEEVENT      gain, state
KEYDOWN          unicode, key, mod
KEYUP            key, mod
MOUSEMOTION      pos, rel, buttons
MOUSEBUTTONUP    pos, button
MOUSEBUTTONDOWN  pos, button
JOYAXISMOTION    joy, axis, value
JOYBALLMOTION    joy, ball, rel
JOYHATMOTION     joy, hat, value
JOYBUTTONUP      joy, button
JOYBUTTONDOWN    joy, button
VIDEORESIZE      size, w, h
VIDEOEXPOSE      none
USEREVENT        code


Pygame handles all its event messaging through an event queue. The routines
in this module help you manage that event queue:
pygame.event.pump	—	internally process pygame event handlers
pygame.event.get	—	get events from the queue
pygame.event.poll	—	get a single event from the queue
pygame.event.wait	—	wait for a single event from the queue
pygame.event.peek	—	test if event types are waiting on the queue
pygame.event.clear	—	remove all events from the queue
pygame.event.event_name	—	get the string name from and event id
pygame.event.set_blocked	—	control which events are allowed on the queue
pygame.event.set_allowed	—	control which events are allowed on the queue
pygame.event.get_blocked	—	test if a type of event is blocked from the queue
pygame.event.set_grab	—	control the sharing of input devices with other applications
pygame.event.get_grab	—	test if the program is sharing input devices
pygame.event.post	—	place a new event on the queue
pygame.event.Event	—	create a new event object
pygame.event.EventType	—	pygame object for representing SDL events
"""
