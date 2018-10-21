#!/usr/bin/python3

d = { "ming" : 15, "hong": 8, "song":9, "lingling":12}

print(d)


# sorted(iterable, key=None, reverse=False) --> return sorted list
#
#  python3 removed cmp argument
#
#   key :  def key_func(a) --> return weight-of-a
#   reverse : false increasing,  true decreasing;


# use key to sort()
d = sorted(d)
print(d)


# use value to sort
def weight(e):
    return e[1]

d = sorted(d, key=weight)
print(d)





d = sorted(d, key=lambda e:e[1])
print(d)
