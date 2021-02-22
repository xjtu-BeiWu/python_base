# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/21 11:51
# File: multiprocessing_pool.py
# IDE: PyCharm

# pool用来完成多进程，将要运行的东西直接放入进程池中。

import multiprocessing


def job(x):
    return x*x


def multi_process():
    pool = multiprocessing.Pool(processes=3)
    res = pool.map(job, range(10))
    print(res)
    # apply_async：只能传递一个值，它只会放入一个核进行运算，注意参数是可迭代的，要加','
    res2 = pool.apply_async(job, (2,))
    print(res2.get())
    results = [pool.apply_async(job, (i,)) for i in range(10)]
    print([result.get() for result in results])


if __name__ == '__main__':
    multi_process()
