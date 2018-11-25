#!/usr/bin/python3

import sys

for i in (sys.argv):
    print(i)


print("=========================\n")


for i in range(0, len(sys.argv)):
    print("argv[%d]: "%(i), sys.argv[i])




