#!/usr/bin/python3

"""
继承(Inherit)

父类(基类，超类)
子类(派生类)
"""

class People:
    def __init__(self, name="unkown", gender="x"):
        self.name = name
        self.gender = gender

    def info(self):
        print("name=%s, gender=%s" %(self.name, self.gender))


class Student(People):
    def __init__(self, name="unknown", gender="x", stuID=0):
        self.name = name
        self.gender = gender
        self.stuID = stuID


class Teacher(People):
    def __init__(self, name="unknown", gender="x", teachID=0):
        self.name = name
        self.gender = gender
        self.teachID = teachID


class Foo(People):
    pass



print("\n==========================")
s1 = Student("ling", "female", 13)
s1.info()
print("s1.name=%s, s1.gender=%s, s1.stuID=%d" %(s1.name, s1.gender, s1.stuID))

print("\n==========================")
t1 = Teacher("Guo", "male", 1)
t1.info()

print("\n==========================")

s1 = Student("ling", "female", 13)
print("s1 is an instance of Teacher ? ", end="")
print(isinstance(s1, Teacher))

print("s1 is an instance of Student ? ", end="")
print(isinstance(s1, Student))

print("s1 is an instance of People ? ", end="")
print(isinstance(s1, People))

print("s1 is a subclass of People ?", end="")
print(issubclass(s1.__class__, People))
