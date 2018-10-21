#!/usr/bin/python3
# -*- coding: utf-8 -*-

nums = [
        4, 13, 84, 159, 163, 246, 269, 288, 
        319, 333, 340, 350, 362, 378, 402, 403, 
        428, 445, 460, 479, 493, 494, 496, 509, 
        524, 530, 532, 555, 556, 570, 587, 613, 
        638, 657, 658, 680, 767, 820, 835, 849, 
        853, 859, 863, 870, 890, 903, 981, 983, 
        988, 996]


# 折半查找

def binary_search(key):
    low = 0
    high = len(nums) -1
    while (low <= high):
        i = (low + high) // 2
        print("low=%d, high=%d, mid=%d" %(low, high,i))
        if nums[i] == key:
            return i;
        if nums[i] < key:
            low = i + 1
        else:
            high = i -1
    return -1


ret = binary_search(4)
print("position=%d, value=%d" %(ret,nums[ret]))

# pratice:  implement the sort algorithm as a func

