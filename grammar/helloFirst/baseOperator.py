# 算术运算符
print(1 + 1)
print(1 - 1)
print(2 * 4)
print(1 / 2)
print(11 // 2)  # 整除运算
print(11 % 2)  # 取余运算
print(2 ** 2)  # 幂运算
print(2 ** 3)

# 特殊算术
print(-9 // -4)

# 一正一负的整数公式，向下取整
print(9 // -4)
print(-9 // 4)

# 余数=被除数-除数*商
print(9 % -4)  # -3
print(-9 % 4)  # 3

# 赋值运算符
# 链式赋值
a = b = c = 20
print(a, b, c, id(a), id(b), id(c))
# 参数赋值
a += 10
print(a, b, c, id(a), id(b), id(c))
# 解包赋值
a, b, c = 10, 20, 30
print(a)
print(b)
print(c)
# 交换
a, b = b, a
print(a, b)

# 比较运算符
aa = 20
bb = 20
print('aa>bb', aa > bb)
print('aa<bb', aa < bb)
# == 比较对象value
print(aa == bb)
# is,is not比较对象标识
print(aa is bb, id(aa), id(bb))
print(aa is not bb)

# bool运算符
a, b = 1, 2
# and
print(a == 1 and b == 2)
# or
print(a == 1 or b == 3)
# not
print(not False)
print(not True)
# in/not in
print('w' in 'world')
print('w' in 'hello')
print('w' not in 'hello')

# 位运算
print(4 & 8)  # 0
print(4 | 8)  # 12
print(4 << 1)
print(2 >> 1)
