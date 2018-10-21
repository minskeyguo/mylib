#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
1. 列表是一个有序的元素集合，列表中的每个元素可以是任何数据类型。

2. 每个元素有一个下表(也叫索引, 序号), 用 "列表名[下标]"的形式访问单个元素, 

3. 可以对列表中的单个元素进行修改插入。
"""



# 混合元素列表
li = [1]

li.append(2)
print(li)

li.append("I love cartoon")
print(li)

print("len(li)=%d" %len(li))

li.append(["list2"])
print(li)

print("删除索引1所在的元素")
li.pop(1)
print(li)


# list.insert(index, value)
# list.append(value)
# list.reserve()
# list.sort()
# list.pop()

