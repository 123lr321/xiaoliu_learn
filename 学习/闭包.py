
def count():
    fs = []
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1,4):
        fs.append(f(i))
    return fs

"""

def count():
    fs = []
    for i in range(1, 4):
        # 使用 lambda 函数创建嵌套函数
        f = lambda: i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())
"""

"""
def count():
    def g(j):
        def inner():
            return j*j
        return inner
    list_1 = []
    for i in range(1,4):
        list_1.append(g(i))
    return list_1

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
"""
def counts():
    fs = []
    for i in range(1, 4):
        # 使用 lambda 函数创建嵌套函数
        f = lambda: i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


f1,f2,f3=counts()
print(f1(),f2(),f3())
