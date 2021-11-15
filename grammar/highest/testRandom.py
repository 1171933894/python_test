# random
# demo1 生成随机数
import random
print(random.random()) # 0到1之间
print(random.uniform(9, 10))  # 0到1之间
print(random.randint(1, 2))  # randint是表示[1, 2]
print(random.randrange(0, 100, 10))  # 步长是10
x = ['CSDN', 'hyuanxin', 'Python']
print(random.choice(x))

# demo2 打乱列表
y = range(100)
z = list(y)
print(z)
random.shuffle(z)
print(z)

# demo3 取样
x = ['CSDN', 'hyuanxin', 'Python']
y = random.sample(x, 1)
print(y)
y = random.sample(x, 1)
print(y)
y = random.sample(x, 1)
print(y, type(y))