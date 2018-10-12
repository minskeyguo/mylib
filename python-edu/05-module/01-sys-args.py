#!/usr/bin/python3

import sys

for i in (sys.argv):
    print(i)


print("=========================\n")

for i in range(0, len(sys.argv)):
    print("argv[%d]: "%(i), sys.argv[i])


print("=========================\n")
print("__file__=%s" %__file__)
print("__name__=%s" %__name__)

