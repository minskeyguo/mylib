#!/usr/bin/python3
# -*- coding: utf-8 -*-

list1 = [246,903,983,849,863,403,524,570,340,494,657,890,532,13,530,362,319,556,853,996,402,4,555,163,479,445,288,988,460,509,350,587,981,638,859,767,658,84,613,870,493,428,378,680,333,835,496,269,159,820]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 选择排序:  每次在未排序的序列中，选出最大的数，放到剩余未排序排序的起始位置
#
"""
从大到小:
    外循环中，i是从0开始到len-1, 所以，已排序的序列将会位于位置i之前.也即是说，
    外循环每次开始迭代时，nums[0] ~ nums[i-1]是已排序序列； nums[i] ~ nums[len-1]
    是未排序序列。这种情况，每次内循环结束，需要从nums[i] ~ nums[len-1]中找出
    的最大数/最小数，放到nums[i]的位置上，从而使得nums[0] ~ nums[i]变为已知的
    有序序列。
"""


def sort_select_1(nums):
    l = len(nums)
    for i in range(0, (l - 1)):
        index = i    # index 记录未排序序列中最大元素的索引（位置)，初始设置为i, 如果找到比nums[i]更大的，更新这个索引值
        for j in range(i + 1, l):
            if nums[j] < nums[index]: # 练习: 从大到小 (秩序把比较时的>修改为<)
                index = j
        nums[index], nums[i] = nums[i], nums[index]


"""
下面把每次选出的最大值（最小值）放到最后. 可以作为作业
"""
def sort_select_2(nums):
    l = len(nums)
    for i in range(l-1, 0, -1):
        index = i    # index 记录未排序序列中最大元素的索引（位置)
        for j in range(i-1, -1, -1):
            if nums[j] > nums[index]:
                index = j
        nums[index], nums[i] = nums[i], nums[index]


"""
下面把每次选出的最大值（最小值）放到最后. 可以作为作业
"""
def sort_select_3(nums):
    l = len(nums)
    for i in range(0, l-1):
        index = l -1 - i    # index 记录未排序序列中最大元素的索引（位置)
        for j in range(0, l - 1 - i):
            if nums[j] > nums[index]:
                index = j
        nums[index], nums[l - i -1] = nums[l - i -1], nums[index]



if __name__ == "__main__":
    print("sort_select_1:")
    sort_select_1(list1)
    print(list1)

    print("\nsort_select_2:")
    sort_select_2(list1)
    print(list1)

    print("\nsort_select_3:")
    sort_select_3(list1)
    print(list1)
