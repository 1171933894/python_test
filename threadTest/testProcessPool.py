import os
from multiprocessing import Pool
from multiprocessing import Process
import time
from random import random

# 进程池分类阻塞式和非阻塞式

# 非阻塞式进程
def task(task_name):
    print('开始做任务啦!', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    print('完成任务!用时:', (end - start), os.getpid())
    return task_name

container=[]
def callback_func(n):
    container.append(n)

# if __name__ == '__main__':
#     pool = Pool(5)
#     tasks = ['听歌', '洗衣服', '打游戏', '散步']
#     for i in tasks:
#         pool.apply_async(task, args=(i,), callback=callback_func)
#     pool.close()
#     pool.join() # 不然主进程停止会导致进程池停止
#     print(container)
#     print('over!!!')

# 非阻塞式
# if __name__ == '__main__':
#     pool = Pool(5)
#     tasks = ['听歌', '洗衣服', '打游戏', '散步']
#     for i in tasks:
#         pool.apply(task, args=(i,)) # 添加一个执行一个，顺序执行
#     pool.close()
#     pool.join()
#     print('over!!!')


# 队列的使用
from multiprocessing import Queue
q = Queue(5)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5) # put 为阻塞方法
print(q, q.qsize())
if not q.full():
    print(q.put(123))
else:
    print('队列已满')

# 进程间通信
def download(q):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:', image)
        time.sleep(1)
        q.put(image, timeout=5)
def getfile(q):
    while True:
        try:
            file = q.get(timeout=5)
            print('正在保存:', file)
        except Exception:
            break
if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
