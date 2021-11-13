name = '张三'
age = 20

# 连接+要求连接内容必须类型相同，否则会报错
print(type(name), type(age))
print(name + str(age))

# 类型转换函数
a = 10
b = 182.9
c = False

print(str(a), str(b), str(c), type(str(a)), type(str(b)), type(str(c)))
print(int(a), int(b), int(c), type(int(a)), type(int(b)), type(int(c)))
print(float(a), float(b), float(c), type(float(a)), type(float(b)), type(float(c)))
