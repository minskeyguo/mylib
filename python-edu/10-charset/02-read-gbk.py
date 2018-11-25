#!/usr/bin/python3
# -*- coding:utf-8 -*-

import codecs
import sys

if len(sys.argv) > 1:
    FILE=sys.argv[1]
else:
    FILE="qing-tong-kui-hua-gbk.txt"

# gb18303, gbk, gb2312, 
fp = codecs.open(FILE, 'r', 'gb18030')
texts = fp.read()
fp.close()


print(texts)
f2 = open("asdfasdf.txt","w")






