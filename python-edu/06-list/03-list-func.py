#!/usr/bin/python3
# -*- coding: utf-8 -*-




lt = [1, 2, 3, 4, 5,6 ]
print("list is: ", end="")
print(lt)

print("len(lt) = %d" %len(lt))
print("min(lt) = %d" %min(lt))
print("max(lt) = %d" %max(lt))
print("sum(lt) = %d" %sum(lt))


lt.append(3.1415926)
print(lt)
print("len(lt) = %d" %len(lt))
print("min(lt) = %d" %min(lt))
print("max(lt) = %d" %max(lt))
print("sum(lt) = %d" %sum(lt))


# 等数据类型不同时，会出错
lt.append("python-test")
print(lt)
print("len(lt) = %d" %len(lt))
print("min(lt) = %d" %min(lt))
print("max(lt) = %d" %max(lt))
print("sum(lt) = %d" %sum(lt))

