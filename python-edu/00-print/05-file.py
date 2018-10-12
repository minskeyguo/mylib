#!/usr/bin/python3

# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

a="www"
b="google"
c="com"

f=open("f.txt", 'w')

print(a, b, c)
print(a, b, c, sep='.', file=f)
print(a, b, c, sep='-', file=f)
print(a, b, c, sep='*********')


