"""
进程创建
导入
process对象=Process（target=函数，name=进程名字，args=（函数参数）必须是一个序列）
process.start()启动任务与进程（主进程与已生成的子进程之间来回切换）
process,run()只执行任务，未启动进程(不能来回切换)
terminate（）终止
自定义进程就是重写继承Process类自定义类，重写__init__及run方法（还要用start调用哦）


"""
from multiprocessing import Process
from time import sleep
import os

class Myprocess(Process):
    def __init__(self,s):
        super(Myprocess,self).__init__()
        self.s=s
    def run(self):
        global m
        while True:
            print('任务二开始')
            m += self.s
            sleep(self.s)
            print("任务二----》", os.getpid(), "-------", os.getppid(), 'm值为：{}'.format(m))


m=1
def task1(s):
    global m
    while True:
        print('任务一开始')
        m+=s
        sleep(s)
        print("任务一----》",os.getpid(),"-------",os.getppid(),'m值为：{}'.format(m))

"""
def task2(s):
    global m
    while True:
        print('任务二开始')
        m+=s
        sleep(s)
        print("任务二----》",os.getpid(),"-------",os.getppid(),'m值为：{}'.format(m))
        """

if __name__ == '__main__':
    print(os.getpid())
    p=Process(target=task1,name="任务1",args=(3,))
    p.start()
    print(p.name)
    p1=Myprocess(2)
    p1.start()
    print(p1.name)
    while True:
        m+=1
        sleep(2)
        print(m,"zzzzzzzz")
        if m>10:
            p.terminate()
            p1.terminate()
            break
    if m==10:
        p.terminate()
        p1.terminate()
    else:
        print(m,"----->")

