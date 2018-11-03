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
        self.__name = name
        self.__gender = gender
        self._age = 0

    def getName(self):
        return self.__name

    def _info(self):
        print("%s's age is : %s" %(self.__name, self._age))


class Student(People):

    def __init__(self, name="", gender="x", stuID=0):
        super(Student, self).__init__(name, gender)
        self.__stuID = stuID

s1 = Student("ling", "female", 13)
s1._info()
s1._age = 99
s1._info()

