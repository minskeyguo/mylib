#!/usr/bin/python3

import argparse
from PIL import Image




ascii_char = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def get_char(r, g, b, a = 256):
    if a == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 *b)
    uint = (256.0 + 1) / length

    return ascii_char[int(gray/uint)]

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('--width', type = int, default=80)
    parser.add_argument('--height', type = int, default =80)
    parser.add_argument('--output')
    args = parser.parse_args()

    img = Image.open(args.file).convert('RGBA')
    img = img.resize((args.width, args.height), Image.NEAREST)

    text = ""
    for i in range(args.height):
       for j in range(args.width):
           r, g, b, a= img.getpixel((j,i))
           text += get_char(r, g, b, a)

       text += '\n'
    print(text)


    if args.output:
        with open(args.output, 'w') as f:
            f.write(text)
    else:
        with open('ascii_img.txt', 'w') as f:
            f.write(text)


'''
把字符看作是比较大块的像素，一个字符能表现一种颜色，字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。


灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。


使用灰度值公式将像素的 RGB 值映射到灰度值sRGB IEC61966-2.1: gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b

创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号

'''
