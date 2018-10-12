#!/usr/bin/python3

num1 = 99
num2 = 77
num3 = 33

print(num1)

#=======================================
# fail, num1 is an integer instead of a string
print("num = " %num1)

# ok
# print("num = " + str(num1))
# print("num = %d" %num1)
#=======================================


print("num1 = %d, num2 = %d" %(num1, num2))
print("num1 = %d, num2 = %d, num3 = %d" %(num1, num2, num3))
