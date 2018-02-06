import os, time, random
# from multiprocessing import Process
from multiprocessing import Pool, Queue, Process
import subprocess

"""
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
然后，分别在父进程和子进程内返回。子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，
一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()
就可以拿到父进程的ID
"""

print('Process (%s) start...' % os.getpid())

# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 子进程输入内容
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

"""
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
"""


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # print('Parent process %s.' % os.getpid())
    # p = Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')
    """
    对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
    调用close()之后就不能继续添加新的Process了。
    task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，
    这是因为Pool的默认大小是CPU的核心数目，因此，最多同时执行4个进程。
    这是Pool有意设计的限制，并不是操作系统的限制。
    """
    # print('Parent process %s.' % os.getpid())
    # p = Pool()
    # for i in range(5):
    #     p.apply_async(long_time_task, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')

    #############################进程间通信
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
