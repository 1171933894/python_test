# 驻留机制
a = 'Python'
b = '''Python'''
c = "Python"
print(id(a))
print(id(b))
print(id(c))

# PyCharm对字符串进行了优化处理
a = 'abc%'
b = 'abc%'
print(a == b)
print(a is b)

# 运行过程不驻留
a = 'abc'
b = 'ab' + 'c'
c = ''.join(['ab', 'c'])
print(a is b)
print(a is c)
print(id(a), id(b), id(c))

# -5到256也是会驻留
na = 5
nb = 5
print(na is nb, id(na), id(nb))

# 查询子串操作
s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

# 大小写转换
# 转大写
print(s.upper())
# 转小写
print(s.lower())
# 首字母大写，其余小写
print(s.capitalize())
# 大小写交换
print(s.swapcase())

# 对齐操作
print(s.center(40, '*'))
print(s.center(40))
print(s.ljust(40, "*"))
print(s.ljust(40))
print(s.rjust(40, "*"))
print(s.rjust(40))
print(s.zfill(40))
# 注意：0会被添加到-号以后
print('-123'.zfill(40))

# 字符串的分割
s = 'hello world Python'
lst = s.split()
print(lst, type(lst))
s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split('|'))
print(s1.split(sep='|', maxsplit=1))  # ['hello', 'world|Python']
print(s1.rsplit('|'))
print(s1.rsplit(sep='|', maxsplit=1))  # ['hello|world', 'Python']

# 字符判断相关方法
s = 'hello, python'
# 是否是合法标识符
print('1.', s.isidentifier())
# 是否全部是空格或者\t或\n
print('1.', ' \t'.isspace())
# 是否是字母/汉字
print('abc'.isalpha())
print('张三'.isalpha())
# 是否是十进制数
print('123'.isdecimal())
# 是否是数字
print('123'.isnumeric())
# 是否全部是数字或字母
print('颤三123'.isalnum())

# 字符替换
s = 'hello,Python,Python,Python,Python'
# 全部替换
print(s.replace('Python', 'Java'))
# 配置最大替换次数
print(s.replace('Python', 'Java', 2))
# 字符合并
lst = ['hello', 'java', 'Python']
print(''.join(lst))
print('|'.join(lst))

t = ('hello', 'java', 'Python')
print(''.join(t))
print('|'.join(t))

# 字符串当作列表
print('*'.join('Python'))

# 字符的比较
print('apple' > 'app')  # True
print('apple' > 'banana')  # False
print(ord('a'), ord('b'))
print(ord('杨'))
print(chr(97), chr(98))
print(chr(26472))

# 字符切段
s = 'hello,Python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newStr = s1 + s3 + s2
print(newStr)

# 格式化字符串
name = '张三'
age = 30
# 使用%
print('我叫%s,今年%d' % (name, age))
# 使用{}
print('我叫{0},今年{1}'.format(name, age))
# 使用f-string
print(f'我叫{name},今年{age}')
# %f
print('%10.3f' % 3.1415926)
print('{0:.3}'.format(3.1415926))  # .3表示的是一共是3位数
print('{0:.3f}'.format(3.1415926))  # .3f表示的是3位小数
print('{0:10.3f}'.format(3.1415926))  # .3f表示的是3位小数，10表示宽度

# 编码
s = '宇宙第一'
print(s.encode(encoding='GBK'))  # 在GBK中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8，一个中文占三个字节
# 解码
rs = s.encode(encoding='GBK')
print(rs.decode(encoding='GBK'))
