#!/usr/bin/python3

"""
对象的域（实例变量）代表了对象的状态，修改变量，就修改了实例的状态。当把
一个对象作为参数传给其他函数时，其他函数可能会错误的修改实例变量，需要控
制访问（封装）--数据隐藏

以双下划线"__" 开头的变量是私有变量，类外部不能直接访问

以下划线“_" 开头的变量是保护变量，子类可以访问，但是非子类的类外部不能直接访问

以双下划线开头和结尾的变量是系统变量
"""

class People:

    def __init__(self, name="", gender="x"):
        self.name = name
        self.gender = gender

    def info(self):
        print("%s's gender is %s" %(self.name, self.gender))

def bad_func(s):
    s.gender = "male XXXXXXXXXXXXXXXXXX"


"""
# 为了防止 bad_func() 这种错误修改类的成员变量的行为，把要保护的
# 成员变量名加上"__"双下划线, 从而变成私有成员
# 
class People:

    def __init__(self, name="", gender="x"):
        self.__name = name
        self.__gender = gender

    def info(self):
        print("%s's gender is %s" %(self.__name, self.__gender))

def bad_func(s):
    s.__gender = "male XXXXXXXXXXXXXXXXXX"

"""


s1 = People("ling", "female")
s1.info()

bad_func(s1)
s1.info()



# print(dir(s1))
