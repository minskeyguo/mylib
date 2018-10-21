#!/usr/bin/python3

# 用圆括号将一些元素括起来就是元组，这些元素可以是数字、字符串

t0 = ()

# 只有一个元素时，必须加一个逗号，否则是无法区分是否是运算用的括号
t1 = (1,)

t2 = (1, 2, 3)
print("t0 is: ", end="")
print(t0)
print("t1 is: ", end="")
print(t1)
print("t2 is: ", end="")
print(t2)


print("t2[0]=", end='')
print(t2[0])

t4 = (1, "string", 333)
print(t4)

# error: 元组不能被修改
t2[2] = 6
