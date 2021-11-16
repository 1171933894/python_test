# 协程实现
# 使用生成器来实现
import time

def task1():
    for i in range(3):
        print('A' + str(i))
        yield
        time.sleep(1)

def task2():
    for i in range(3):
        print('B' + str(i))
        yield
        time.sleep(2)

# if __name__ == '__main__':
#     g1 = task1()
#     g2 = task2()
#
#     while True:
#         try:
#             next(g1)
#             next(g2)
#         except:
#             break

# 使用greenlet完成协程任务
'''
from greenlet import greenlet
def a():
    for i in range(5):
        print('A' + str(i))
        gb.switch()
        time.sleep(0.1)
def b():
    for i in range(5):
        print('B' + str(i))
        gc.switch()
        time.sleep(0.1)
def c():
    for i in range(5):
        print('C' + str(i))
        ga.switch()
        time.sleep(0.1)

if __name__ == '__main__':
    ga = greenlet(a)
    gb = greenlet(b)
    gc = greenlet(c)
    ga.switch()  # 启动协程'''
