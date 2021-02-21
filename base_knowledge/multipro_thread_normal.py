# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/21 10:50
# File: multipro_thread_normal.py
# IDE: PyCharm


# 进行多进程、多线程、正常运行代码时间效率对比

import multiprocessing as mp
import threading as mt
import time


def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res)


def multi_process():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multi_process: ', res1+res2)


def multi_thread():
    q = mp.Queue()
    t1 = mt.Thread(target=job, args=(q,))
    t2 = mt.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multi_thread: ', res1+res2)


def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i ** 2 + i ** 3
    print('normal: ', res)


if __name__ == '__main__':
    start_time1 = time.time()
    multi_process()
    print('multi_process time: ', time.time()-start_time1)
    start_time2 = time.time()
    multi_thread()
    print('multi_thread time: ', time.time()-start_time2)
    start_time3 = time.time()
    normal()
    print('normal time: ', time.time()-start_time3)


# 结果为：multi_process:  499999666667166666000000
# multi_process time:  1.3519532680511475
# multi_thread:  499999666667166666000000
# multi_thread time:  2.37261962890625
# normal:  499999666667166666000000
# normal time:  2.184154987335205
