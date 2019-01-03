#!/usr/bin/python3

import sys
from PIL import Image


# ascii_char = "1234567890"
ascii_char = "1234567890 "
ascii_char = "1234567890abcdefghijklmnopqrstuvwxyz "

def get_char(r, g, b, a = 256):
    if a == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 *b)
    uint = (256.0 + 1) / length

    return ascii_char[int(gray/uint)]

WIDTH = 64
HEIGHT = 64
if __name__ == "__main__":
    img_file = sys.argv[1] 

    img = Image.open(img_file).convert('RGBA')
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    text = ""

    for i in range(HEIGHT):
       for j in range(WIDTH):
           r, g, b, a= img.getpixel((j,i))
           text += get_char(r, g, b, a)

       text += '\n'
    print(text)


