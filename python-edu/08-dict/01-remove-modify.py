#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# key:value pair
d = {"lingling":12, "dudu" : 12, "jiajia":12}
print(d)

print("删除佳佳")
del d["jiajia"]
print(d)


print("更新凌凌")
d["lingling"] = 13
print(d)
