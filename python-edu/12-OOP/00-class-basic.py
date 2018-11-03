#!/usr/bin/python3

"""
对象和类： 
  对象是特征和行为的集合。 一个人，一只羊等都是一个对象；世间万物都是对象。 把同一种类的所有对象加以抽象，用属性(变量）表示特征，方法（函数）表示行为，这些属性和方法作为一个集合，就是类(class).  类的每个实例就是一个对象。
  
类: 对象的集合。它定义了该集合中每个对象所共有的属性和方法。 我们可以把类看做一个模板（模具），用模板构造处理的实例就是对象

类的3大特征：封装，继承，多态
1. 封装
   
   1.1 属性
       实例变量 属于对象 在内存中，每个对象有一份copy
       类变量   属于类  在内存中，只有一份，属于类
   1.2 方法

类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重载：从父类派生出子类时，如果父类的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（overrstuIDe）

实例变量：定义在方法中的变量，只作用于当前实例的类。

继承：派生类继承基类）的属性和方法。继承允许把一个派生类的对象作为一个基类对象对待。

实例化：创建一个类的实例。

方法：类中定义的函数。




面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
"""

class Student:

    def __init__ (self, name="unknown", stuID=0):
        """
        相当于构造函数，完成初始化
        """
        self.name = name
        self.stuID = stuID
        print("calling Student.__init__: name=%s" %name)

    def __del__ (self):
        """
        相当于析构函数
        """
        print("__del__ is being called: name=%s" %self.name)

    def talk(self):
        print("%s is talking" %self.name)

    @staticmethod
    def run():
        print("run() is a static method")

if __name__ == "__main__":

    s1 = Student("ling", 13)    # 创建实例
    s1.talk()
    Student.talk(s1)
    print('\nUsing "del s1" to delete s1')
    del s1

    print("\n========================")
    s2 = Student("dudu", 3)  #创建实例
    s2.talk()
    Student.talk(s2)

    # 调用静态方法
    s2.run()
    Student.run()

# print(dir(Student))



