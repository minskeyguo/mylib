#!/usr/bin/python3
# -*- coding: utf-8 -*-

nums = [246,903,983,849,863,403,524,570,340,494,657,890,532,13,530,362,319,556,853,996,402,4,555,163,479,445,288,988,460,509,350,587,981,638,859,767,658,84,613,870,493,428,378,680,333,835,496,269,159,820]

# 冒泡排序 
for i in range(len(nums) - 1):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]


# nums.sort()

print(nums)

# exercise:  implement the sort algorithm as a func

