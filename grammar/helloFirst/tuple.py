# 元组创建
# 使用()
t = ('Python', 'world', 98)
print(t)
print(type(t))

# 使用tuple函数
t1 = tuple(('Python', 'world', 98))
print(t1)

# 省略()
t2 = 'Python', 'world', 98
print(t2)
print(type(t2))

# 如果元组只有一个元素，必须加上逗号
t3 = ('Python',)
print(t3)
print(type(t3))

t4 = ()
t5 = tuple()
print(t4)
print(t5)

# 元组读取元素（可变对象内部数据可变）
t6 = (1, [3, 4], 2)
print(t6[1])
t6[1].append(5)
print(t6[1])

# 元组遍历
for item in t:
    print(item)

