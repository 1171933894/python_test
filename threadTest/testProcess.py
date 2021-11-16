# 创建进程
from multiprocessing import Process
from time import sleep
import os

# 测试多个进程是否能共享同一个空间（答案：否）
m = 1

def task1(s):
    global m
    while(True):
        sleep(s)
        m+=1
        print('这是任务1...', os.getpid(), os.getppid(), m)

def task2(s):
    global m
    while(True):
        sleep(s)
        m += 1
        print('这是任务2...', os.getpid(), os.getppid(), m)

# if __name__ == '__main__':
#     # task1无法结束，task2无法开始
#     # task1()
#     # task2()
#     p1 = Process(target=task1, name='任务1',args=(1,))
#     p2 = Process(target=task2, name='任务2',args=(2,))
#     # 调用run方法没法使用
#     # p1.run()
#     # p2.run()
#     # 开启进程
#     p1.start()
#     print(p1.name)
#     p2.start()
#     print(p2.name)
#
#     number=1
#     while True:
#         number+=1
#         sleep(1)
#         m+=1
#         print('这是主线程m=', m)
#         if number==10:
#             p1.terminate()
#             p2.terminate()
#             print('主进程终止子进程')
#             break
#
#     print('主进程在干活', os.getpid(), os.getppid())

# 自定义进程
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name
    # 重写run方法
    def run(self):
        while True:
            sleep(1)
            print('-----指定义进程', self.name)

if __name__ == '__main__':
    p1 = MyProcess('小明')
    p2 = MyProcess('小红')
    p1.start()
    p2.start()