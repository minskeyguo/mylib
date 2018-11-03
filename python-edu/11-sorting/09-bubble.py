#!/usr/bin/python3
# -*- coding: utf-8 -*-

num = [246,903,983,849,863,403,524,570,340,494,657,890,532,13,530,362,319,556,853,996,402,4,555,163,479,445,288,988,460,509,350,587,981,638,859,767,658,84,613,870,493,428,378,680,333,835,496,269,159,820]

num2 = [1, 2, 3, 4, 5]
num3 = [1, 2, 3, 4, 5]

# 冒泡排序 
def sort_bubble_1(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def sort_bubble_2(lst):
    n = len(lst)
    for i in range(n - 1):
        exchange = False       # <-----------------
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                exchange = True   # <-------------
        print("i=%d, exchange=%d" %(i, exchange))


def sort_bubble_3(lst):
    n = len(lst)
    for i in range(n - 1):
        exchange = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                exchange = True
        print("i=%d, exchange=%d" %(i, exchange))
        if not exchange:  break     # <============


if __name__ == "__main__":
  sort_bubble_1(num)
  print(num)

  print("\n==============================")
  sort_bubble_2(num2)
  print(num2)

  print("\n==============================")
  sort_bubble_3(num2)
  print(num3)

