#!/usr/bin/python3
#coding=utf-8 

"""
bytes is a series of byte, 
string is a series of character (a char might be 1, 2, 3, 4, bytes)

bytearray 
"""


c = u"中"

print("c=%c, unicode-code=0x%x(%d)" %(c, ord(c), ord(c)))

print("default encode: ", c.encode())

# encode() is to do: str --> bytes
bytes_utf8 = c.encode("utf-8")
print("utf8:  ", bytes_utf8)

bytes_utf16 = c.encode("utf-16")
print("utf16:  ", bytes_utf16)

bytes_utf32 = c.encode("utf-32")
print("utf32:  ", bytes_utf32)

print("gb2312:  ", c.encode("gb2312"))
print("gbk:  ", c.encode("gbk"))
print("gb18030:  ", c.encode("gb18030"))
