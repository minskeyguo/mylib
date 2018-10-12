#!/usr/bin/python3

for num in range(20, 40): 
   for i in range(2, num):
       if num % i == 0:
          j = num / i         
          print("%d = %d * %d" %(num, i, j))
          break
   else:
      print (num, '是质数')
