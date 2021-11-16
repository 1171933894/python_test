# 线程创建
import threading
import time
from time import sleep

def download(n):
    images=['girl.jpg', 'boy.jpg']
    for image in images:
        print('正在下载:', image)
        sleep(n)

t = threading.Thread(target=download, name='aa', args=(1,))
# t.start()

# 线程同步，通过lock函数
lock = threading.Lock()
list1 = [12,23,34]*10
# print(list1)

def task1():
    lock.acquire()
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release()

def task2():
    lock.acquire()
    for i in range(len(list1)):
        print('--->', list1[i])
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t2.start()
    t1.start()
