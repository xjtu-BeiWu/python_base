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
    # multi_process()
    # shared memory
    value = multiprocessing.Value('i', 0)
    # 这里的Array和numpy不一样，只能是一维的，不能是多维的
    array = multiprocessing.Array('i', [1, 2, 3])

# | Type code | C Type             | Python Type       | Minimum size in bytes |
# | --------- | ------------------ | ----------------- | --------------------- |
# | `'b'`     | signed char        | int               | 1                     |
# | `'B'`     | unsigned char      | int               | 1                     |
# | `'u'`     | Py_UNICODE         | Unicode character | 2                     |
# | `'h'`     | signed short       | int               | 2                     |
# | `'H'`     | unsigned short     | int               | 2                     |
# | `'i'`     | signed int         | int               | 2                     |
# | `'I'`     | unsigned int       | int               | 2                     |
# | `'l'`     | signed long        | int               | 4                     |
# | `'L'`     | unsigned long      | int               | 4                     |
# | `'q'`     | signed long long   | int               | 8                     |
# | `'Q'`     | unsigned long long | int               | 8                     |
# | `'f'`     | float              | float             | 4                     |
# | `'d'`     | double             | float             | 8                     |
