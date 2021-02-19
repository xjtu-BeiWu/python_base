# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/19 21:49
# File: threading_lock.py
# IDE: PyCharm

# lock在不同线程使用同一共享内存时，能够确保线程之间互不影响。
# 比如当打印结果是交替打印时，但是如果需求是需要打印完一个线程的内容后，再去打印另一个线程的内容，就需要用到lock。
# 在每个线程执行运算修改共享内存之前，
# lock.acquire()：将共享内存上锁，确保当前线程执行时，内存不会被其他线程访问。
# 执行运算完毕后，
# lock.release()：将锁打开，保证其他的线程可以使用该共享内存。

import threading


def t1():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('t1: ', A)
    lock.release()


def t2():
    global A, lock
    lock.acquire()
    for i in range(10):
        A += 1
        print('t2: ', A)
    lock.release()


if __name__ == '__main__':
    A = 0
    lock = threading.Lock()
    thread1 = threading.Thread(target=t1, name='t1')
    thread2 = threading.Thread(target=t2, name='t2')
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
