#!/usr/bin/python3


str1 = "this"
str2 = "is"
str3 = "a"
str4 = "dog"



print(str1)
print(str2)
print(str3)
print(str4)


print(str1, end="")
print(str2, end="")
print(str3, end="")
print(str4, end="")




print("")
for i in range(1, 5):
    for j in range(1, 5):
        if j>=i:
            print(" * ", end='')
    print("\n")

# *   *   *   *
# *   *   *
# *   *
# *
