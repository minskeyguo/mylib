#!/usr/bin/python3


s1 = "abcxyzABCXYZ"
for ch in s1:
    print("%c -->%d   0x%x" %(ch, ord(ch), ord(ch)))

print("")

s2 = "0123456789"
for c in s2:
    print("%c -->%d   0x%x" %(c, ord(c), ord(c)))
