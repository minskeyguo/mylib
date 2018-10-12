#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
def funcName(parameters):
    statement
    return [expression]
'''

def doOneMul( ):
    a = int(input("输入被乘数: "))
    b = int(input("输入乘数: "))
    print("%d * %d = ? " %(a, b), end="")
    c = input()
    if int(a) * int(b) == int(c):
        return True
    else:
        return False


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



def doFewMulWithScore(count):
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

