#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
希尔排序(Shell Sort)是一种插入排序, 又称“缩小增量排序”. 是直接插入排序算法的一种更高效的改进版本
希尔排序是非稳定排序算法。该方法因D.L.Shell于1959年提出而得名。
希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含
的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止

先取一个小于n的整数d1作为第一个增量，把文件的全部记录分组。所有距离为d1的倍数的记录放在
同一个组中先在各组内进行直接插入排序；然后，取第二个增量d2<d1重复上述的分组和排序，直至
所取的增量dm=1(dm<  …<d2<d1)，即所有记录放在同一组中进行直接插入排序为止。

该方法实质上是一种分组插入方法. 一般选择 Len/2, len/4 ..., 1
"""


num=[246,903,983,849,863,403,524,570,340,494,657,890,532,13,530,362,319,556,853,996,402,4,555,163,479,445,288,988,460,509,350,587,981,638,859,767,658,84,613,870,493,428,378,680,333,835,496,269,159,820]


"""
50 个元素
                       距离    25，   12，     6，  3，   1,
对应的每个分组内元素个数是：    2     4,5     8,9  16,17  50

"""

def sort_shell(num):
    n = len(num)

    # 生成距离列表
    gaps = []
    d = n // 2
    while d > 0:
        gaps.append(d)
        d = d // 2

    print("the gaps we choose:", end="\t")
    print(gaps)

    # 对生成的每个距离做迭代
    for g in gaps:
        for i in range(g, n):
            tmp = num[i]
            j = i

            # 简单插入排序
            while j >= g and num[j - g] > tmp:
                    num[j] = num[j - g]
                    j -= g
            num[j] = tmp



if __name__ == "__main__":
    sort_shell(num)
    print(num)


