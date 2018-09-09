
import struct
import sys

def uint8(f):
    return ord(f.read(1))

def uint16(f):
    return struct.unpack("<H", f.read(2))[0]

def uint32(f):
    return struct.unpack("<I", f.read(4))[0]

def uint64(f):
    return struct.unpack("<Q", f.read(8))[0]

def varInt(f):
    prefix = uint8(f)
    if prefix < 0xfd:
        return prefix
    if prefix == 0xfd:
        return uint16(f)
    if prefix == 0xfe:
        return uint32(f)
    if prefix == 0xff:
        return uint64(f)

def sha256(f):
    return bytes(f.read(32))

# transform bytes/string to hex-string with space seperated for displaying
def toHexString(a):
    if sys.version_info < (3, 0):
        return " ".join("%02x" %(ord(n)) for n in a)
    else:
        return " ".join("%02x" %(n) for n in a)

