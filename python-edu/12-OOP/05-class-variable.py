#!/usr/bin/python3

"""
# 通过一个对象a访问一个类变量x时: python 先在对象自身的__dict__中查找是
# 否有x，如果有则返回，否则进入对象a所属于类中的__dict__中进行查找

# 对象a试图修改一个属于类的immutable的变量，则python会在内存中为对象a
# 新建一个变量，此时a就具有了属于自己的实例变量
"""

class Student:
    StudentNums = 0   # <=== 类变量，同一个类的所有对象(实例)共有，只有一份
    test = 99
    
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
print("s1.name=%s, s1.stuID=%d, s1.StudentNums=%d" %(s1.name, s1.stuID, s1.StudentNums))

s2 = Student("dudu", 2)
print("s2.name=%s, s2.stuID=%d, s2.StudentNums=%d" %(s2.name, s2.stuID, s2.StudentNums))

print("Student.StudentNums=%d" %Student.StudentNums)

print("\n==============================")

# 通过对象S1/S2访问一个类变量test: python 先在对象自身的__dict__中查找是
# 否有x，如果有则返回，否则进入对象s1/s2所属的类中的__dict__中进行查找
# 由于是读，共享一个类变量
print("s1.test = %d, s2.test=%d, Student.test =%d" %(s1.test, s2.test, Student.test))

# 对象s1试图修改一个属于类的immutable的变量，会创建一个s1的实例变量
s1.test = 100
print("s1.test = %d, s2.test=%d, Student.test =%d" %(s1.test, s2.test, Student.test))
