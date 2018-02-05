from enum import Enum, unique
from types import MethodType

"""
任何模块代码的第一个字符串都被视为模块的文档注释
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，
__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，
我们自己的变量一般不要用这种变量名；
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，
是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，
从编程习惯上不应该引用private函数或变量

object类是所有类的父类;
方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，
虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
只有内部可以访问，外部不能访问;

双下划线开头的私有属性也是可以访问的，类似JAVA的反射技术；
不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，
仍然可以通过_Student__name来访问__name变量,但是不同版本的Python解释器可能会把__name改成不同的变量名

可调用对象（callable），我们平时自定义的函数、内置函数和类(类本身)都属于可调用对象，但凡是可以把一对括号()
应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable
如果在类中实现了 __call__ 方法，那么实例对象也将成为一个可调用对象

类的定制话：
https://docs.python.org/3/reference/datamodel.html#special-method-names
"""


class Student(object):
    # 类属性
    name = 'Student'

    # 在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
    # 并且调用时，不用传递该参数;self 相当于JAVA中的this；__init__相当于构造器
    def __init__(self):
        self.__name = "name"

    #     定义好__str__()方法，返回一个自定义的有意义的字符串
    # __repr__()是为调试服务的,因此 __repr__ = __str__
    def __str__(self):
        pass

    """
    如果一个实例本身可以被执行，是因为其实现了__call__()方法；函数会被执行，是因为函数本身也是一个对象，
    其本身也是实现了__call__()方法；
    """

    def __call__(self):
        print('My name is %s.' % self.name)


# 创建实例
stu1 = Student()
# 实例属性优先级比类属性高，因此它会屏蔽掉类的name属性,但是类属性并未消失，用Student.name仍然可以访问
# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
stu1.name = "stud"
"""
外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的self.__name
变量不是一个变量！内部的self.__name变量已经被Python解释器自动改成了_Student__name，
而外部代码给bart新增了一个__name变量
"""
stu1.__name = "__name"

"""
开闭原则：
对扩展开放：允许新增Animal子类；
对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，
那它就可以被看做是鸭子。
Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like 
object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

获得一个对象的所有属性和方法，可以使用dir()函数
hasattr函数判断是否存在属性
setattr函数设置属性的值
getattr函数获取属性的值
getattr(obj, 'z', 404)404表示在属性不存在时返回的值
"""
print(dir(Student))


def set_age(self, age):
    pass


stu1.set_age = MethodType(set_age, stu1)  # 给实例绑定一个方法
Student.set_age = set_age  # 为类绑定方法，从而每个实例都会有这个方法

"""
一个特殊的__slots__变量，来限制该class实例能添加的属性
__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
"""

"""
MixIn的目的就是给一个类增加多个功能，
这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
只允许单一继承的语言（如Java）不能使用MixIn的设计。
"""

"""
如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的
下一个值，直到遇到StopIteration错误时退出循环
"""

"""
__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，
还有一个__delitem__()方法，用于删除某个元素。
总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，
这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
"""


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


class Student(object):

    def __init__(self):
        self.name = 'Michael'

    # 当调用类的属性或者方法不存在时，__getattr__(self, 'score')来尝试获得属性或者方法
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
