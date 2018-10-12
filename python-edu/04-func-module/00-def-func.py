#!/usr/bin/python3
# -*- coding: UTF-8 -*-


#####################################################################
#    Step by Step, add more functionalities into self-defined func:
#
# def funcName(parameters):
#    statement
#    return [expression]
#####################################################################


"""
####### Step 1 #######
def doMul(a, b):
    c = a * b
    return c

e = input("num 1: ")
f = input("num 2: ")

p = doMul(e, f)
printf("product = %d" %p)
"""



"""
####### Step 2 #######
def doMul( ):
    a = input("num 1: ")
    b = input("num 2: ")
    c = a * b
    return c

p = doMul( )
printf("product = %d" %p)

"""


"""
####### Step 3 #######
def doMul( ):
    a = int(input("输入被乘数: "))
    b = int(input("输入乘数: "))
    print("%d * %d = ? " %(a, b), end="")
    c = input()
    if int(a) * int(b) == int(c):
        return True
    else:
        return False

ok = 0
for i in range(0, 3):
    ret = doMul()
    if ret == True:
        ok += 1

print("你做对了%d道题" %ok)

"""


"""
####### Step 4 #######
def doFewMul(count):
    ok = 0
    for i in range(0, count):
      a = int(input("输入被乘数: "))
      b = int(input("输入乘数: "))
      print("%d * %d = ? " %(a, b), end="")
      c = input()
      if int(a) * int(b) == int(c):
          ok = ok + 1
    return ok

num = doFewMul(2)
print("你做对了%d道题" %num)
"""


"""
####### Step 5 #######
def doFewMul(count):
    ok = 0
    fail = 0
    for i in range(0, count):
      a = int(input("输入被乘数: "))
      b = int(input("输入乘数: "))
      print("%d * %d = ? " %(a, b), end="")
      c = input()
      if int(a) * int(b) == int(c):
          ok = ok + 1
      else:
          fail = fail+1
    return ok, fail

t, f = doFewMul(2)
print("你做对了%d道题, 错了%d道题" %(t, f))
"""


def doFewMul(count):
    ok = 0
    fail = 0
    for i in range(0, count):
      a = int(input("输入被乘数: "))
      b = int(input("输入乘数: "))
      print("%d * %d = ? " %(a, b), end="")
      c = input()
      if int(a) * int(b) == int(c):
          ok = ok + 1
      else:
          fail = fail+1
    return ok, fail


if __name__ == "__main__":
    t, f = doFewMul(2)
    print("你做对了%d道题, 错了%d道题" %(t, f))





