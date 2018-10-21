#!/usr/bin/python3

d = { "ming" : 15, "hong": 8, "song":9, "lingling":12}
print("before sorted(d):  ", end="")
print(d)


# sorted(iterable, key=None, reverse=False) --> return sorted list
#
#  python3 removed cmp argument
#
#   key :  def key_func(a) --> return weight-of-a
#   reverse : false increasing,  true decreasing;


# use key to sort()
d = sorted(d)
print("after sorted(d):  ", end="")
print(d)




# use value to sort
def weight(e):
    return e[1]

d = { "ming" : 15, "hong": 8, "song":9, "lingling":12}
print("before sorted(d, key=weight):  ", end="")
print(d)
d = sorted(d, key=weight)
print("after sorted(d, key=weight):  ", end="")
print(d)


d = { "ming" : 15, "hong": 8, "song":9, "lingling":12}
print("before sorted(d.keys():  ", end="")
print(d)
d = sorted(d.keys(), key=lambda e:e[1])
print("after sorted(d.keys():  ", end="")
print(d)
