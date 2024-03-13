def outer():
    print('我是外部')

    def inner():
        print('我是内部')
    return inner


# 这是闭包，返回一个函数
def outer_2():
    print('我是外部')

    def inner_2():
        print('我是内部')

    return inner_2()


# 这个狗屁不是，return一个函数但是直接运行了
"""
def decorators(func):
    def slap():
        func()
        print('给刘润一个大耳巴子')

    return slap


@decorators
def house():
    print('lunrun')
    print('困了')



house()
这个是不带参数的装饰器
"""

"""
def decorators(func):
    def slap(a):
        func(a)
        print('给刘润一个大耳巴子')

    return slap


@decorators
def house(a):
    print(a, 'lunrun')
    print('困了')


house(12)
这个是带参数的装饰器，house输入的函数会被slap接受，并也可以在slap内引用
注意，函数本身的返回值会在装饰器内部函数调用，而
"""
"""
def decorators(func):
    def list_exchange(*args, **kwargs):
        return *args,kwargs

    return list_exchange


@decorators
def str_exchange(a):
    return list(a)


e = '123'
print(str_exchange(e))
注意，这里内部函数接受了是*args和**kwargs，我们把参数打包进装饰器里的内部函数使用，注意别忘记拆包哦
"""

# 拆包

test = [1, 2, 3]
a = [*test]
print(a)


# 装包

def a(*args, **k):
    print(args, k)


#当装饰器也需要参数时，你就需要多加一层装饰了，因为decorator里面要装函数，所有要再加一层用来承接你的函数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator
def decorators(func):
    def list_exchange(*args, **kwargs):
        return *args,kwargs

    return list_exchange


@decorators
def str_exchange(a):
    return list(a)


e = '123'
print(str_exchange(e))