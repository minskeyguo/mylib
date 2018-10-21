#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# key:value pair
d = {"lingling":12, "dudu" : 12, "jiajia":12}
print(d)

# error#1
print("试图访问不存在的键值")
print(d["baba"])


# error#2 
print("使用了同一个键值")
d = {"ling":12, "ling":13}
print(d)

