# 单例模式：
# 开发模式：单例模式
# 固定对象地址
class Singleton:
    __instance = None

    def __new__(cls,name,age):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            # object.__new__用于产生地址
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name, age):
        self.name = name
        self.age = age
liu=Singleton('liurn',18)
print(liu,liu.name,liu.age)
xuy=Singleton('xy',22)
print(xuy,xuy.name,xuy.age,liu,liu.name,liu.age)
