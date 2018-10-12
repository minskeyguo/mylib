#!/usr/bin/python3
# -*- coding: UTF-8 -*-

num = 0;

while num < 4:
    print("Question：%d * %d  = ?" %(num, num))
    product = input("answer：")
    product = int(product)
    if  num * num == product:
        break;
    num = num + 1
else:
    print("你全做错了")




"""
homework:
  1. add the functionatlity to the file: 
             computing the times of right answers

  2. when  5 times ok, exit;
"""
