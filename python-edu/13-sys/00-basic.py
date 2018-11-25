#!/usr/bin/python3
# coding: utf-8

import sys

"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

用IDLE shell查看下面的属性：
sys.argv: 实现从程序外部向程序传递参数。

sys.exit([arg]): 程序中间的退出，arg=0为正常退出。

sys.getdefaultencoding(): 获取系统当前编码，一般默认为ascii。

sys.setdefaultencoding(): 设置系统默认编码，执行dir（sys）时不会看到这个方法，在解释器中执行不通过，可以先执行reload(sys)，在执行 setdefaultencoding('utf8')，此时将系统默认编码设置为utf8。（见设置系统默认编码 ）

sys.getfilesystemencoding(): 获取文件系统使用编码方式，Windows下返回'mbcs'，mac下返回'utf-8'.

sys.path: 获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。

sys.platform: 获取当前系统平台。

sys.stdin,sys.stdout,sys.stderr: stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们
"""

print(sys.__name__)

print(sys.__package__)

print(sys.__dir__)


# print(sys.__dict__)
# print(sys.__doc__)

print (sys.version)

print(sys.path)


