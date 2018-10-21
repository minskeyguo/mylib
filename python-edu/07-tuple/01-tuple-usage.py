#!/usr/bin/python3

# 学籍管理的一条记录
# (name, gender, age)

team = { ("ling", "female", 12), ("dudu", "female", 12), ("jiajia", "male", 12)}

print("name\t gender\t age")
print("---------------------")
for e in team:
    print("%s\t %s\t %d" %(e[0], e[1], e[2]))




