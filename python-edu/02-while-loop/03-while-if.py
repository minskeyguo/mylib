#!/usr/bin/python3
# -*- coding: UTF-8 -*-


num = 0;

while num < 5:
    print("Question：%d * %d  = ?" %(num, num))
    product = input("answer：")
    product = int(product)
    if  num * num == product:
        print("Good")
    else:
        print("Bad")
    num = num + 1



"""
homework:
  1. add the functionatlity to the file: 
             computing the times of right answers

  2. when  5 times ok, exit;
"""
