#!/usr/bin/python3




import time

# timestamp时间戳，时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量
now0=time.time()
print(now0)


# struct_time元组， 9元组
now1 = time.localtime()
print(now1)

now2 = time.gmtime()
print(now2)

# struct_time to timestamp
now10=time.mktime(now1)
print(now10)

# timestamp to struct_time
now01=time.localtime(now0)
print(now01)



print(time.ctime())

# format time  Y-year, m-month, d-day, H/h-(24/12)hour, M-minutes, S-second, X localtime
print(time.strftime("%Y-%m-%d %X"))

"""
# STEP: 2

import datetime

# datetime is a wrapper of time module
# datetime.date(year, month, day)
# datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ) 

"""



"""
STEP: 3


import pygame, sys, time
from pygame.locals import *

FPS=0.5 

pygame.init()
c = pygame.time.Clock()

# set up the window
surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

while True: # the main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

    c.tick(FPS)
#    t = time.time()
#    print("run %d" %t)

"""
