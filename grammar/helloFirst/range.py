# range函数
r = range(10)
print(r)  # range对象
print(list(r))  # 用来查看range对象中的整数序列
 # 结合in使用
print(2 in r)
print(2 in list(r))
print(20 in list(r))
print(20 not in list(r))