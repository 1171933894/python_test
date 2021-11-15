# map函数的使用
def lifang(x):
    return x ** 3

a = [1, 2, 3, 4]
y = map(lifang, a)
print(y, type(y), list(y))

# reduce函数的使用
from functools import reduce
def mini(x, y):
    return x if x > y else y
a = [123, 123, 123, 123, 12312, 3123, 12234, 345, ]
y = reduce(mini, a) # 其原理是一个一个比较
print(y)