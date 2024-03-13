"""
面向对象
程序    现实中
对象   具体的事物
现实中的事物-->电脑程序
世间万物皆对象

好处：
满足复用
灵活性更高
面向对象：
类（手机类）
对象（刘润的手机、苒苒的手机、张三的手机）
属性（品牌、颜色、大小、价格）
方法（打电话、发短信、上网、打游戏）
多个对象--》提取对象的共同的特征和动作--》封装到一个类中
"""

"""
# 所有类名要求首字母大写并驼峰式命名
class Phone:
    brand = 'huawei'

    def __init__(self, note):
        self.note = note

    def call(self):
        print('self----->', self)
        print(self.note)

    @classmethod
    def leitest(cls):
        cls.brand = 'xiaomi'

    def __str__(self):
        return self.note


phone = Phone('123')
phone.note = '我是phone的note'
phone1 = Phone('ws')
phone.call()
phone1.call()
phone2 = phone1
del phone2
print('没有调用类方法之前', phone1.brand)
phone1.leitest()
print('调用类方法之后', phone.brand)
print(phone)
"""
"""
liurun = Phone()
zhangsan = Phone()
liurun.brand = 'iphone'
print(zhangsan.brand, liurun.brand)
"""
# 类属性，对象属性
"""
类中方法：动作
种类： 普通方法  类方法  静态方法  魔术方法
普通方法格式：
def 方法名（self [,参数，参数]):
    pass
__init__（self，参数）默认必执行且第一个执行（可用来传递对象属性）
类方法格式：
@classmethod
def 方法名（cls）:
    pass

特点：
依赖装饰器
参数为类（cls)
不依赖对象可直接使用（不可出现对象属性）
可使用类属性
不可使用普通方法

作用：
实现在对象创建之前需完成的动作

静态方法：类似于类方法
需要装饰器@staticmethod
无需传递参数
只能访问类的属性和方法，对象无法访问
类与静态区别
装饰器不同
有无参数
相同
只访问类不访问对象
创建对象之前，不依赖对象



魔术方法（满足一些条件自动触发，无需调用）
__call__
(对象当成函数使用（默认执行和__init__一样，但是只有当函数使用才可以））
__del__
对象赋值（phone1=phone）phone1指向phone地址
del删除对象引用（指针删除）
python底层代码自带执行垃圾回收内存释放（删除没有任何引用的空间）
__str__
如果想在打印对象是展示更多信息，在__str__中return信息
"""
# 加_可以使类里的属性不能在外部修改，只能在内部修改（通过类方法）
# 私有化
""" 
封装：私有化属性、定义公有的set及get方法
_属性就是将属性私有化，访问范围限于类中(定义类中的修改及显示方法，保证数据正确）
"""


class Student:
    score = 59

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def kind_test(cls, score_modify):
        cls.score = score_modify

    @staticmethod
    def static_test(c):
        Student.score = c

    def __str__(self, *args, **kwargs):
        return "年龄为{}的学生{}的分数为{}".format(self._age, self._name, self.score)

    def name_set(self, name_modify):
        self._name = name_modify
"""
私有化
这是等价的
@property
def name(self)
  return self._name
@name.setter(self,name_modify)
  self._name=name_modify  
"""


class Xuyue(Student):
    def __init__(self, name, age, personality):
        print('我是子类init')
        super().__init__(name, age)
        self.personality = personality

    def __str__(self):
        return "{}是{}".format(self._name,self.personality)


# 如何调用父类的__init__加一个suoer（）.__init__(其它方法也可以super（）.方法名）注意，父类的参数要通过子类的参数输入，注意可以只传一部分参数到父类
# 如果子类和父类有重复方法，优先调用子类（调用时均会优先调用子类）


xy = Xuyue('徐越', 16, "色情大魔头")
xy.static_test(44)
print(xy)

liurun = Student('刘润', 18)
print(liurun)
Student.static_test(78)
print(liurun)
liurun.name_set('lr')
print(liurun)
# 开发中私有化处理：装饰器@perperty
# @property
# def get（）
# return私有化的属性(将其公有化）
# @get.setter（依赖于上面的get）
# def modify()
# 对其进行修改
"""
类中创建的对象也是一种类型，可被其他类或函数应用
has a
一个类对象中属性也可以使用另一种自定义类型
类型：系统类型，自定义类型


is a base class 父类  基类
继承：
多个类可能存在相同属性或方法
提取相同属性形成父类
继承：class 函数（父类）
python允许多继承
多继承搜索顺序
经典类（不加object）主流：
广度优先（二叉树后序遍历）
python2（加object）
从左至右，深度优先（二叉树中序遍历）
"""
