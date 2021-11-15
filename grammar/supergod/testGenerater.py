# 生成器语法1
print('生成器语法1')
def gen(n):
    for i in range(n):
        # return 2*i # 如果使用return只会有一个0被返回
        yield 2 * i
a = gen(6)
print(a)
for i in a:
    print(i)
print()

# 生成器语法2 简化版本
print('生成器语法2')
gen = (i*i for i in range(5))
for i in gen:
    print(i)