# 创建函数
def calc(a, b):
    print('a=', a, ',b=', b)
    c = a + b
    return c


# 调用函数
result = calc(10, 20)
print(result)

result = calc(b=10, a=20)
print(result)


# 函数返回多个值为元组
def fun(num):
    odd = []  # 奇数列表
    even = []  # 偶数列表
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even;


print(fun([i for i in range(1, 11)]))


# 参数默认值
def fun1(a, b=10):
    return a + b
print(fun1(10))
print(fun1(10, 100))

# 可变参数
# *可变形参
def fun2(*args):
    print(args)
fun2(1)
fun2(1, 2, 3)
# **字典形参
def fun3(**args):
    print(args)
fun3(a=10)
fun3(a=10, b=20)

# 函数调用特例
def fun4(a,b,c):
    print(a,b,c)
fun4(10,20,30)
lst=[20,30,40]
fun4(*lst) # 函数调用时，将列表中每个元素都转换为实参传入
d = {'a':'a',"b":'b',"c":"c"}
fun4(**d)
# 要求a和b使用位置行程，c和d必须使用关键字行程
def fun5(a, b, *, c, d):
    print(a, b, c, d)
fun5(1, 2, d=3, c=4)

# 递归函数
# 计算阶乘
def fac(num):
    if num == 1:
        return 1
    else:
        return fac(num - 1) * num
print(fac(1))
print(fac(5))
# 斐波拉西数列
def fib(n):
    if n ==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print('fib(5)', fib(5))