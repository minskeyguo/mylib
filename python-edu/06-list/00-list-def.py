#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
1. 列表是一个有序的元素集合，列表中的每个元素可以是任何数据类型。

2. 每个元素有一个下表(也叫索引, 序号), 用 "列表名[下标]"的形式访问单个元素
   第一个元素的下标为0

3. 可以对列表中的单个元素进行修改插入。
"""

l = []

# 整数列表
list0 = [1, 2, 3]
print(list0)

# 字符列表
list1 = [ 'a', 'b', 'c',]
print(list1)


#字符串列表
list2 = [ "abc", "def", "ghi", "jkl", "mn"]
print(list2)


# 混合元素列表
list3 = ["a", "this is a car", 1, 2, "Failed"]
print(list3)

print("=============================================")

# 列表的列表
list4 = [1, "a string", list3]
print("list4 is:  ", end="")
print(list4)
print("\n")

print("Each element of list4 is: ")
for i in range(0, len(list4)):
    print("\tlist4[%d]: " %i, end="")
    print(list4[i])
