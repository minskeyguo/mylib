#!/usr/bin/python3

"""
运行时创建实例变量和类变量
"""

class Student:
    StudentNums = 0   # <=== 类变量，同一个类的所有对象(实例)共有，只有一份
    
    def __init__(self, name="", stuID=0):
        self.name = name
        self.stuID = stuID
        Student.StudentNums += 1

    def __del__(self):
        Student.StudentNums -= 1

    def getName():
        return self.name

    def getStuID():
        return self.stuID


s1 = Student("ling", 13)

       

# add an age attribute to s1
s1.age = 13
print("s1.age=%d" %s1.age)

# error, we just added age attribute to s1, not to s2
print("s2.age=%d" %s2.age)


Student.grade = 1
print("Student.grade=%d" %Student.grade)
print("s1.grade=%d" %s1.grade)
print("s2.grade=%d" %s2.grade)
