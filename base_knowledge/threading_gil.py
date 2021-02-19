# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/19 21:16
# File: threading_gil.py
# IDE: PyCharm

# Global Interpreter Lock (GIL)让 Python 还是一次性只能处理一个东西，一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行
# GIL只会影响到那些严重依赖CPU的程序（比如计算型的），如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适。
# https://mofanpy.com/tutorials/python-basic/threading/GIL/

import threading
from queue import Queue
import copy
import time


def job(d, q):
    res = sum(d)
    q.put(res)


def multithreading(d):
    threads = []
    q = Queue()
    for i in range(4):  # 4个线程
        thread = threading.Thread(target=job, args=(copy.copy(d), q), name='T%i' % i)  # 用了shallow copy
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    results = 0
    for _ in range(4):
        results += q.get()
    print(results)


def normal(d):
    results = sum(d)
    print(results)


if __name__ == '__main__':
    data = list(range(1000))
    start_time = time.time()
    normal(data*4)  # list直接复制四次
    print('normal: ', time.time()-start_time)
    start_time = time.time()
    multithreading(data)
    print('multithreading: ', time.time()-start_time)

# 测试结果为：
# 1998000
# normal:  0.000225067138671875
# 1998000
# multithreading:  0.0015919208526611328
# 很奇怪为什么反而是多线程的慢？？？！！！