"""
进程池：各进程按顺序进入进程池，
pool（）
非堵塞式：pool.apply_async
要加上pool.close pool.join
非堵塞式：全部添加至队列中，完成一个出去一个进来一个，并未等其他进程执行完毕
callback
堵塞式：pool.apply
也要加上pool.close pool.join
callback=函数：当targe函数有返回值可以利用callback添加返回值操作
进程使用方式和非堵塞式一样，但是必须一个一个进入进程池，直到上一个执行完毕
"""
import os
import time
from multiprocessing import Pool
from random import random
from multiprocessing import Queue



def task(task_name):
    print('现在开始进行的任务是：', task_name)
    start = time.time()
    time.sleep(random() * 2)
    end = time.time()
    print( "完成任务用时时长：", task_name, end - start, os.getpid())
#    return "完成任务用时时长：", task_name, end - start, os.getpid()


"""
这是非阻塞式，多组并进
# 回调方法

def callback_func(n):
    print(n)

if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,),callback=callback_func)
    pool.close()
    pool.join()
    print('任务完成咯')
"""
if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7']
    for task1 in tasks:
        pool.apply(task, args=(task1,))
    pool.close()#关闭进程池
    pool.join()#让主进程让步（插队）
    print('任务完成咯')
q=Queue(5)
q.put(1)
print(q.qsize())
q.put(1)
q.put(1)
q.put(1)
q.get(1)