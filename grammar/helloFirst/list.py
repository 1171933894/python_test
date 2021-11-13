# list表示列表
lst = ['1', '2', 3]
lst = list(['1', '2', 4])
print(id(lst))
print(type(lst))
print(lst)
# 从前到后，下标从0开始；
# 从后往前，下标从-1开始
print(lst[2], lst[-1])

# index函数找不到会抛异常
print(lst.index('2'), )
print(lst.index('2', 0, 3))

# 列表的切片
lst = [10, 20, 30, 40, 50, 60]
print('原列表', id(lst), lst)
lst1 = lst[1:4:1]
print('切片段', id(lst1), lst1)
lst1 = lst[1:4]
print('切分段', id(lst1), lst1)
lst1 = lst[1:4:2]
lst1 = lst[1:4:]
print('切分段', id(lst1), lst1)
# 负步长表示逆序
lst1 = lst[::-1]
print('切分段', id(lst1), lst1)

# 判断以及遍历
print('p' in 'python')
print('k' not in 'python')
lst2 = [100, 200, 'python']
print(100 in lst2)
for item in lst2:
    print(item)

# 列表元素的增加操作
lst3 = [10, 20, 30]
print('添加元素之前', lst3, id(lst3))
# 末尾添加
lst3.append(100)
print('末尾添加元素', lst3, id(lst3))
# 将列表作为一个元素添加
lst4 = [1, 2, 3]
lst3.append(lst4)
print('末尾添加元素', lst3, id(lst3))
# 末尾一次性添加多个元素
lst3.extend(lst4)
print('末尾添加元素', lst3, id(lst3))
# 在列表某个位置上添加一个元素
lst3.insert(0, 111)
print('在列表某个位置上添加一个元素', lst3, id(lst3))
# 在任意位置上添加N个元素
lst3[1:] = lst4
print('在任意位置上添加N个元素', lst3, id(lst3))

# 删除列表元素
lst3.remove(1)  # 如果有重复元素，那么移除的是第一个元素
print('删除列表元素', lst3, id(lst3))
lst3.pop(0)  # 按照索引来移除，索引不存在会抛出异常
print('删除列表元素', lst3, id(lst3))
lst3.pop()  # 删除最后一个元素
print('删除列表元素', lst3, id(lst3))
# 使用切片可以做到删除，但是会产生一个新对象，如果不想可以使用如下
lst3 = [10, 20, 30]
lst3[1:2] = []
print('删除列表元素', lst3, id(lst3))
# clear()方法清空所有元素
# lst3.clear()
print('删除列表元素', lst3, id(lst3))
# del lst3

# 修改列表元素
# 一次修改一个值
lst3[0] = 11111
print('修改列表元素', lst3, id(lst3))
# 一次修改多个值
lst3[0:3] = [1, 2, 3, 4]
print('修改列表元素', lst3, id(lst3))

# 列表元素排序操作
# 使用sort函数
lst3.sort()  # 默认升序排序
print('排序后的列表', id(lst3), lst3)
lst3.sort(reverse=True)
print('排序后的列表', id(lst3), lst3)
# 使用sorted函数，会新生成列表
lst4 = sorted(lst3)
print('排序后的列表', id(lst4), lst4)
lst4 = sorted(lst3, reverse=True)
print('排序后的列表', id(lst4), lst4)

# 列表生成式
lst6 = [i * i for i in range(1, 10)]
print(lst6)
lst6 = [i * 2 for i in range(1, 10)]
print(lst6, "元素个数", len(lst6))
