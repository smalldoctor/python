import time, threading

"""
_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装

由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例

因为高级语言的一条语句在CPU执行时是若干条语句

threading.Lock() 创建锁
lock.acquire() 获取锁
lock.release() 释放锁

200%的CPU，也就是占用两个CPU核心

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，
多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，
除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，
那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，
互不影响。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
多线程的并发在Python中是不可能的。

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
threading.local() 创建ThreadLocal变量
"""


# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)
