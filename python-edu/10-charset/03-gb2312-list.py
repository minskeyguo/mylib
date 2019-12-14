#!/usr/bin/python3

import sys
import struct

if len(sys.argv) < 2:
    print("Usage: program zone_number\n");
    sys.exit(0);

zone = int(sys.argv[1])

if zone < 0 or zone > 97:
    print("Zone must be 0 ~ 97\n")
    sys.exit(0)
    
try:
    for index in range(1,128):
        code = (zone << 8) + index + 0x2020 + 0x8080
        barray = struct.pack('>H', code)
        chinese = barray.decode(encoding="gb2312")
        print("%x" %code, end=' ')
        print(chinese, end='  ')
        if index % 10 == 0:
            print("\n");
except:
    pass
finally:
    print("\n")

'''
u = 0xb0a1
ba = struct.pack('>H', u)
print(ba.decode(encoding='gb2312'))
'''
