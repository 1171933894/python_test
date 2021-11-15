import heapq

# 将列表转换为堆
x = [4, 5, 6, 7, 9, 1, 2, 3, 0]
print(x)
heapq.heapify(x)
print(x, type(x))
# 添加一个元素
heapq.heappush(x, 2)
print(x)
# 拿出来一个元素
heapq.heappop(x)
print(x)
# heappushpop函数（先放入，再弹出）
item = heapq.heappushpop(x, 7)
print(item)
print(x)
# heapreplace函数（先弹出，在放入）
item = heapq.heapreplace(x, -1)
print(item, type(item))
print(x)

# merge函数
x = [14, 5, 62, 4, 5, 7, 810]
y = [1, 7, 23]
z = heapq.merge(x, y)
print(z, type(z))
print(list(z))

# nlargest和nsmallest
lg = heapq.nlargest(4, x)
print(lg)
sm = heapq.nsmallest(4, x)
print(sm)