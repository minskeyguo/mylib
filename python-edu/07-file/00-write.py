#!/usr/bin/python3


f = open("f.txt", "w")

f.write("This is my first file\n")

f.close()



# when write failed, f.close() won't be called
# so:
#   with open("f.txt", "w") as f
