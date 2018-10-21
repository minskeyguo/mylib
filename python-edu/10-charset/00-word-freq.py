#!/usr/bin/python3
# -*- coding:utf-8 -*-

# unicode: 基本汉字 0x4e00, 0x9fa5

scope = ((0x4e00,0x9fa5),)

FILE="qing-tong-kui-hua.txt"

fp = open(FILE, 'r')
texts = fp.read()
fp.close()

# if isinstance(texts, unicode): print(FILE + ": unicode")

li = []
for ch in texts:
    li.append(ch)

wfreq = {}
pfreq = {}
for w in li:
    if ord(w) > scope[0][0] and ord(w) < scope[0][1]:
        if w in wfreq:
            wfreq[w] += 1
        else:
            wfreq[w] = 1
    else:
        if w in pfreq:
            pfreq[w] += 1
        else:
            pfreq[w] = 1

wfreq = sorted(wfreq.items(), key=lambda x:x[1], reverse=True)
pfreq = sorted(pfreq.items(), key=lambda x:x[1], reverse=True)

for entry in wfreq[:100]:
    print("%s\t: %d" %entry)

for entry in pfreq[:100]:
    print("%s\t: %d" %entry)


print(len(wfreq))

print(len(texts))



