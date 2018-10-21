#!/usr/bin/python3

import random

fp = open("f.txt", "w")

for i in range(50):
    num =random.random() * 1000
    num = int(num)
    fp.write(str(num))
    fp.write(str(" "))

fp.close()


