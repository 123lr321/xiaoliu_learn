# 进程间通信
"""
利用队列以及传参来控制两进程一块进行
"""
"""
import time
from multiprocessing import Process
from multiprocessing import Queue


def download(q):
    img = ['man.jpg', 'wuman.jpg', 'youngman.jpg']
    for i in img:
        print("正在下载：", i)
        time.sleep(0.5)
        q.put(i)


def getfile(q):
    while True:
        try:
            file = q.get(timeout=3)
            print('保存成功', file)
        except:
            break


if __name__ == '__main__':
    q = Queue(5)
    p1 = Process(target=download, args=(q,))
    p2 = Process(target=getfile, args=(q,))
    p1.start()
    p2.start()
    """

# 线程是比进程更小的单元，可以几个线程共享一个进程，线程在进程里面并发执行（轮流使用）


"""
创建线程：threading Thread（同进程）
多个线程可同时对变量进行操作，但因此可能导致不同步：（线程1取变量i，计算出i+1，还未赋值，线程2取变量i，计算出i+1，赋值给i，线程1再赋值给i）
进程只是把共享值取过来，各自拥有一个值
加锁解决（效率降低）（只要有数据共享必须加锁）
python底层默认加锁
可以用加锁的方式实现独占，lock.acquire lock.release
可以添加时间限制避免死锁
进程：计算密集型
线程：耗时操作 爬虫
"""
import threading
import time
money=100
lock=threading.Lock()
def run1(s):
    global money
    lock.acquire()
    for i in range(100):
        print('我是run1，money减：',i)
        time.sleep(s)
        money-=1
    lock.release()
def run2(s):
    global money
    lock.acquire()
    for i in range(100):
        print('我是run2，money减：',i)
        time.sleep(s)
        money-=1
    lock.release()

t1=threading.Thread(target=run1,args=(0.1,))
t2=threading.Thread(target=run2,args=(0.1,))
t1.start()
t2.start()
t1.join()
t2.join()
print(money)


