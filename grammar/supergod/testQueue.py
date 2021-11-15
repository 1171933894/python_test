# 实现队列
from collections import deque
x = deque([9, 7, 8])
print(x)
x.append(666)
print(x)
x.popleft()
print(x)