# -*- coding: utf-8 -*-
from collections import Iterable

a = 100
"""
冒号之后的代码是块代码
"""
if a > 101:
    print(a)
else:
    print(-a)

# list支持反向遍历
# list是可变列表，支持追加，指定位置插入，删除尾部元素等
p = ["asp", "java"]
s = ["go", "c", p, "c++"]
a = p[1]
s = s[2][1]
print(s)
print(a)

# tuple是不可变列表;
# tuple的不变是指tuple中的元素指向不变，并不约束指向的内容发生变化，类似于Java的final变量
t = (1)  # 按照数学计算符 括号
t = (1,)  # 按照tuple定义

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 1
if x:
    print(x)
# python不允许字符串直接和数值进行比较,所以需要注意变量的类型，如input()返回的值是字符串；

# 通过in判断是否存在key
d = {"a": "1", "b": "2"}
print("a" in d)

# set通过list进行初始化
set1 = set([1, 2, 3, 3])

t1 = (1, 2, 3)
d[(1, 2, 3)] = t1
# 下面这个虽然编译没有问题，但执行是有问题的，因为tuple含有一个list元素，list元素本身的内容是可变的；dict要求key是不可以变的
# t2 = (1, [1, 2])
# d[(1, [1, 2])] = t2
print(d)

print(isinstance(1, (int, float)))

abs(-1)

# 函数可以返回多个值，其实是返回的一个tuple；python的变量定义可以多个变量接受一个tuple,每个变量取对应位置的；
r1, r2, r3 = (1, 2, 3)
print(r1)


# 函数定义时可以有多p个参数，为了对遗留代码不影响，可以使用默认参数，默认参数在外界不传时生效
def power(p, n=3):
    return n * p


# l定义的默认参数是列表，列表是对象，是可变的对象，因此每次使用默认值时，都是在改变列表本身
def add_end(l=[]):
    l.append("END")
    return None


# *作用是number可以接受N个参数，N>=0;在函数执行时，number在内部会变成一个tuple；
# *tuple/list是将tuple/list元素作为独立的参数传入函数
def cal(*number):
    pass


'''
**定一个类似与dict的参数，即可以接受N个key-value对作为参数；
在函数内部会将每组key-value组装为dict；
对已经存在的dict，可以使用**将其转换为一组组key-value传入函数，然后python会将每组key-value
组合起来构成新的dict供函数使用；

函数的参数分为：必选参数、默认参数、可变参数、关键字参数和命名关键字参数;
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''


def person(name, age, **kw):
    pass


# *之后的内容，标识指定key名的关键字参数
def person1(name, age, *, city, job):
    pass


# *args是可变参数，因为已经含有*号，所以city，job自动变为指定key名的关键字参数
def person2(name, age, *args, city, job):
    pass


# city是含有默认值的关键字参数，可以在调用时不传入
def person3(name, age, *, city="beijing", job):
    pass


'''
python的函数调用也是通过调用栈帧的方式实现的；防止递归函数，栈溢出；

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

目前python并没有尾递归进行优化，还是存在栈溢出；

python中可以理解分为变量和对象；对象是有类型的，变量是没有类型的；
对象分为可变和不可变两种；
变量相当于一个标签，起到引用的作用，指引对象的作用；
'''


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


L = list(range(10))
print(L)

# 第一个是起始位置，第二个是结束位置(不包括本身，即N-1)；第三个是步长，每几个取一个；
# L = L[0:10:5]
# print(L)
# python中的切片是生成一个新的，对其进行修改不会影响原有的
L1 = L[0:10:5]
L1[0] = 10
print(L1)
print(L)

'''
python中的for循环可以用于任何可迭代的数据结构；
可以通过如下方式判断是否可以迭代;

python中不支持数据类型的隐式转换，需要进行强制类型转换；强制类型转换避免了隐式转换带来的逻辑错误；
'''
print("是否可以迭代： " + str(isinstance([1, 2, 3], Iterable)))

for i, v in enumerate(L):
    print("索引：" + str(i) + " 值:" + str(v))


def modPara(para):
    para = 3
    print("para:" + str(para))


def modlist(para):
    para[0] = 3
    print("para:" + str(para))


int1 = 1
print(int1)
int3 = int1
int1 = 4
print(int1)
print(int3)
modPara(int1)
print("int1:" + str(int1))
list1 = [1, 1, 1]
print("list1:" + str(list1))
modlist(list1)
print("list1:" + str(list1))
