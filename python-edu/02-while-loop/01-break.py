#!/usr/bin/python3


num = 1

############### step 1 ############
while True:
    print("Question: %d * %d = ?" %(num, num))
    answer = input("answer:")
    answer = int(answer)
    num = num + 1



############### step 2 ############
while True:
    print("Question: %d * %d = ?" %(num, num))
    answer = input("answer:")
    answer = int(answer)
    if num * num == answer:
        break;
    num = num + 1
