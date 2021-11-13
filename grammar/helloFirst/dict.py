# 使用花括号
scores = {'张三': 100, '李四': 99}
print(scores)
# 使用dict函数
student = dict(name='jack', age=20)
print(student)
# 空字典
d = {}
print(d)

# 获取元素
# 使用[]，key不存在，抛出valueError
print(scores['张三'])
# 使用get，key不存在，不会报错
print(scores.get('张三'))
# 使用get可以设置默认值
print(scores.get('张三1', 90))

# in判断key是否存在
print('张三' in scores)
print('张三1' in scores)

# del删除某个key
print(scores)
del scores['张三']
print(scores)
# clear清空字典
scores.clear()
print(scores)

scores = {'张三': 100, '李四': 99}

# 新增元素
scores['王五'] = 88
print(scores)

# 修改元素
scores['王五'] = 100
print(scores, type(scores))

# 获取所有key
keys = scores.keys()
print(keys, type(keys))
print(list(keys), type(list(keys)))
# 获取所有value
vals = scores.values()
print(vals, type(vals))
print(list(vals), type(list(vals)))
# 获取所有key-value对
items = scores.items()
print(items, type(items))
print(list(items), type(list(items)))

# 字典元素的遍历
for item in scores:
    print(item, scores[item], scores.get(item))

scores1 = {'张三': 100, '张三': 99}
print(scores1)
print(len(scores1))

# 字典生成式
items = {'Fruits', 'Books', 'Others'}
prices = {96, 98, 45}
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)
