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
        self._name = name
        self.__gender = gender

    def info(self):
        print("gender is : %s" %(self._name))



class Student(People):

    def __init__(self, n="", g="x", stuID=0):
        #
        # self.__name 定义在Student的成员变量，而不是People内. 造成People中
        # __name, __gender没有初始化，为解决这个问题，应改为：
        #
        super(Student, self).__init__(n, g)
        #
        #  把getName(self)的定义移动到People
 #       self.__name = name
 #       self.__gender = gender
        self.__stuID = stuID


    def getName(self):
        return self._name

s1 = Student("ling", "female", 13)
print(s1.getName())

s1.info()

# s2 = People("dudu", "female")
# s2.info()



