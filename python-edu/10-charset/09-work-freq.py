#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

if len(sys.argv) > 1:
    FILE=sys.argv[1]
else:
    FILE="qing-tong-kui-hua.txt"

# unicode: 基本汉字 0x4e00, 0x9fa5
scope = ((0x4e00,0x9fa5),)

fp = open(FILE, 'r')
texts = fp.read()
fp.close()

# if isinstance(texts, unicode): print(FILE + ": unicode")

li = []
for ch in texts:
    li.append(ch)

words = 0
punc = 0
wfreq = {}
pfreq = {}
for w in li:
    if ord(w) > scope[0][0] and ord(w) < scope[0][1]:
        if w in wfreq:
            wfreq[w] += 1
        else:
            wfreq[w] = 1
        words += 1
    else:
        if w in pfreq:
            pfreq[w] += 1
        else:
            pfreq[w] = 1
        punc += 1

wfreq = sorted(wfreq.items(), key=lambda x:x[1], reverse=True)
pfreq = sorted(pfreq.items(), key=lambda x:x[1], reverse=True)

for entry in wfreq:
    print("%s\t: %d  %f" %(entry[0], entry[1], entry[1]/words))

for entry in pfreq:
    print("%s\t: %d" %entry)


print(len(wfreq))

print(len(texts))



