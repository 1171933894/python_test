# 模块导入
import logging
import math

print(type(math))
print(math)
print(math.pi)
print(dir(math))
print(math.pow(2, 3), type(math.pow(2, 3)))
print(math.ceil(9.001), math.floor(9.9999))
from math import pi

print(pi)
print(pow(2, 3))
print(math.pow(2, 3))
# 导入其他模块
import importb

print(importb.calc(1, 2))
print(dir(importb))
print(importb.__name__)
if __name__ == '__main__':
    print('I am is import')

# sys模块的使用
import sys

print(sys.getsizeof(45))
print(sys.getsizeof(False))
print(sys.getsizeof(1))

# time模块
import time

print(time.time())
print(time.localtime(time.time()))

# 操作文件
import os

# 爬虫可以使用
import urllib.request

print(urllib.request.urlopen('http://www.baidu.com').read())

# 使用logging
logging.error("logging.error")