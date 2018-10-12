#!/usr/bin/python3


# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# In python3, input() reture a string
b = input('Enter a number:')

# print("b is: " + str(type(b)))

# type transforming
b = float(b)

# print("b is :" + str(type(b)))

sq = b ** 0.5

print(sq)
print("sq=%f" %sq)
print("sq=%10.5f" %sq)

# fail
# print('The square root of ' + sq)

# ok
# print('The square root of ' + str(sq))
# print('The square root of %f is %f' %(b, sq))


# ok to trying sep argument of print() func
# print("The square root of", str(b), 'is', str(sq))
# print("The square root of", str(b), 'is', str(sq), sep='')
# print("The square root of", str(b), 'is', str(sq), sep='    ')
