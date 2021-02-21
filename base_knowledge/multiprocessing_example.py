# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/21 10:24
# File: multiprocessing_example.py
# IDE: PyCharm

# 运用多核来运行现有python程序，应对threading的劣势。
# 使用方法和多线程比较相似
# 使用Queue来存储多进程/核的结果，因为多进程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果


import multiprocessing


def job():
    print('hello multiprocessing!')


def p(q):
    res = 0
    for i in range(1000):
        res += i + i**2 + i**3
    q.put(res)


if __name__ == '__main__':
    # mp = multiprocessing.Process(target=job)
    # mp.start()
    # mp.join()
    que = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=p, args=(que,))
    p2 = multiprocessing.Process(target=p, args=(que,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = que.get()
    res2 = que.get()
    print(res1+res2)
