import threading
import time

m = 1


def wait(name):
    global m
    m -= 1
    print('wait', name)
    if m < 3:
        while m < 0:
            time.sleep(1)
            print('进程在循环', name)


def sign(name):
    global m
    print('执行完毕', name)
    m += 1


def run(name):
    wait(name)
    print('开始启动', name)
    time.sleep(5)
    sign(name)


if __name__ == '__main__':
    pp1 = threading.Thread(target=run, args=('pp1',))
    pp2 = threading.Thread(target=run, args=('pp2',))
    pp1.start()
    pp2.start()
    pp1.join()
    pp2.join()
