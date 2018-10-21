#!/usr/bin/python3
# -*- coding:utf-8 -*-

import codecs

FILE="qing-tong-kui-hua-gbk.txt"

fp = codecs.open(FILE, 'r', 'gbk')
texts = fp.read()
fp.close()
print(texts)





