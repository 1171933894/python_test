# 集合的创建
s = {1, 2, 3}
print(s)

# 用range函数
s = set(range(6))
print(s)

# 用列表创建
s = set([1, 2, 4, 5, 5, 6, 7])
print(s)

# 用元组创建
s = set((1, 2, 4, 5, 5, 6, 7))
print(s)

s = set('Python')
print(s)

s = set({'Python', 'Hello'})
print(s)

# 不能使用{}
s = set()
print(s)

# 集合相关操作
# in/not in判断操作
s = {1, 2, 3, 4, 5, 6}
print(2 in s)
print(10 in s)
print(10 not in s)

# 集合元素的新增操作
# add方法
s.add(80)
print(s)
# update方法
s.update({200, 300, 400})
s.update([2001, 3001, 4001])
s.update((20011, 30011, 40011))
print(s)

# 集合删除操作
# s.remove(400111) # KeyError:500
s.discard(40011)
print(s)
# pop随机删除
s.pop()
print(s)
# clear清空
s.clear()
print(s)

# 集合关系
s1 = {10, 20, 30, 40}
s2 = {10, 20, 30, 40, 50, 60}
# 两个集合是否相等（元素相同，就相等）
print(s1 == s2)
print(s1 != s2)
# 一个集合是否是一个集合的子集
print(s1.issubset(s2))
# 一个集合是否是一个集合的超集
print(s2.issuperset(s1))
# 两个集合是否含有交集
s3 = {100, 200}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# 交集操作
print(s1.intersection(s2))
print(s1 & s2)
# 并集操作
print(s1.union(s2))
print(s1 | s2)
# 差集操作
print(s2.difference(s1))
print(s2 - s1)
# 对称差集
print(s1.symmetric_difference(s2))

# 集合生成式
s5 = {i for i in range(10)}
print(s5)
