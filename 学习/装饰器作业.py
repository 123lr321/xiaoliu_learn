def decorator(func):
    print('11111')
    def inner(sa, ta):
        print('这是第{}个装饰器'.format(1))
        print('开始运行')

        return func(sa, ta)

    return inner


@decorator
def is_anagram(s, t):
    s_list = list(s)
    t_list = list(t)
    for i in s_list:
        if i in t_list:
            t_list.remove(i)
        else:
            return False
    if t_list:
        return False
    else:
        return True


print(is_anagram('waqw', 'sqw'))


def decorators_2(func):
    def list_exchange(*args,**kwargs):
        return func(*args),*args

    return list_exchange


@decorators_2
def str_exchange(a):
    return list(a)


e = '123'
print(str_exchange(e))
