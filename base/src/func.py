# -*- coding: utf-8 -*-
"""
函数名可以看做变量,一个指向函数的变量；
函数可以赋值给变量
"""
from functools import reduce


def f(x):
    return x * x


"""
python提供map()和reduce()函数，从而支持map/reduce;
map:
map返回是一个Iterator,即迭代器类型的结果，是一个惰性的生成器;map会将函数作用于序列的每个元素；
reduce：
reduce是将函数作用于两个元素的累积；
"""
r = map(f, [1, 2, 3, 4, 5])

print(r)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


l1 = [str(x) for x in range(1, 10)]

print(str2int(l1))

"""
filter函数用于过滤列表的元素,filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列
"""


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    # 返回值是一个lambda表达式
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

"""
sorted函数用于用于对列表进行排序;接受一个函数，函数将作用域列表的
每个元素，然后按照每个元素对应的函数值进行排序，最后展示函数值所对应的原始元素；
list = [36, 5, -12, 9, -21]
keys = [36, 5,  12, 9,  21]===>
keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
"""

"""
python的函数支持返回值是一个函数；每次函数调用返回的函数都是一个新的函数，即返回的函数对象不是同一个；
"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# f1和f2指向的是不同的对象
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 以下三个函数的执行结果都是9；因为闭包的函数在返回时是不会进行计算的，只有在调用时才会计算；
# 所以闭包函数f中的i是以被真正调用时i的值为准，而不是在闭包函数f被返回时就确定的；
f1()
f2()
f3()
"""
返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
"""


def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


"""
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
"""
