#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys

if len(sys.argv) > 1:
    FILE=sys.argv[1]
else:
    FILE="qing-tong-kui-hua.txt"

# unicode: 基本汉字 0x4e00, 0x9fa5
# scope = (0x4e00,0x9fa5)


fp = open(FILE, 'r')
texts = fp.read()
fp.close()

li = []
for ch in texts:
    li.append(ch)


words = 0
punc = 0
wfreq = {}
pfreq = {}
for w in li:
    if ord(w) > eval("0x4e00") and ord(w) < eval("0x9fa5"):
        words += 1
        if w in wfreq:
            wfreq[w] += 1
        else:
            wfreq[w] = 1
    else:
        punc += 1
        if w in pfreq:
            pfreq[w] += 1
        else:
            pfreq[w] = 1



wfreq = sorted(wfreq.items(), key=lambda x:x[1], reverse=True)
for entry in wfreq[ :100]:
#for entry in wfreq:
    print("%s\t: %d  %f" %(entry[0], entry[1], entry[1]/words))


pfreq = sorted(pfreq.items(), key=lambda x:x[1], reverse=True)
for entry in pfreq[ :100]:
# for entry in pfreq:
    print("%s\t: %d" %entry)


print("使用汉字%d个，不同汉字%d个，平均每个汉字使用了%d次" %(words, len(wfreq), words/len(wfreq)))
print("使用标点符号%d个，不同标点%d个，平均每个标点使用了%d次" %(punc, len(pfreq), punc/len(pfreq)))

print("总的字符数：%d" %len(texts))



