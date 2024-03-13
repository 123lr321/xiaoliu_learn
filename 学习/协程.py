"""
z协程：微线程
耗时操作（网络请求，网络下载，IO操作）
"""
# 利用yield生成器多任务切换
# greenlet（人工切换） gevent(只要有IO操作自动切换）（猴子补丁遇到耗时操作自动切换）也可以
"""
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
"""
import  requsets
