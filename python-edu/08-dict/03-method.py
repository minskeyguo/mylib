#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# key:value pair
d = {"lingling":12, "dudu" : 12, "jiajia":12}
print(d)

# 返回元组
l = d.items()
print("d.items() return: ", end="")
print(l)

keys = d.keys()
print("d.keys() return: ", end="")
print(keys)

v = d.values()
print("d.values() return: ", end="")
print(v)
