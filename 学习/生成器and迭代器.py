"""def func():
    for i in range(10):
        yield i"""
# g = (i for i in range(3))
"""
print(g.__next__())
print(next(g))
print(next(g))
获取生成器元素的两种方式
获取全部元素可以用循环完成
"""
"""
while True:
    try:
        print(next(g))
    except:
        print('没有更多元素')
        break
        """
"""
如果函数出现yield，则相当于返回一个生成器
斐波那契数列
"""


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        temp = yield b
        print(temp)
        a, b = b, a + b
        n += 1
    for x in range(temp):
        print('-----', x)
        print('*********')
    return '没有更多元素了'


c = fib(7)
n0 = c.send(None)
n1 = c.send(7)
print('www', n0, n1)
while True:
    try:
        print(next(c))
    except:
        print('没有更多元素')
        break
# 利用yield生成器多任务切换
def f1(n):
    for i in range(n):
        print('f1的第{}次'.format(i))
        yield
def f2(n):
    for i in range(n):
        print('f2的第{}次'.format(i))
        yield
g1=f1(5)
g2=f2(5)
while True:
    try:
        next(g1)
        next(g2)
    except:
        pass
        break
