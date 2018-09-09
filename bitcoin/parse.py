#!/usr/bin/python3


import sys
import os

from block import Block

print(sys.version_info)


def parse(fblock):
    b = Block(fblock)
    print(b)
    print("read %d byte" %(fblock.tell()))

    b = Block(fblock)
    print(b)
    print("read %d byte" %(fblock.tell()))
    
    b = Block(fblock)
    print(b)
    print("read %d byte" %(fblock.tell()))


def main():
   # print(list(sys.path))
    if len(sys.argv) < 2:
        print("input the file name of BTC blockchain file\n")
        sys.exit()

    with open(sys.argv[1], "rb") as f:
        parse(f)

if __name__ == "__main__":
    main()
