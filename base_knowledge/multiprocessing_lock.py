# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/22 10:16
# File: multiprocessing_lock.py
# IDE: PyCharm

# shared memory
# value = multiprocessing.Value('i', 0)
# 这里的Array和numpy不一样，只能是一维的，不能是多维的
# array = multiprocessing.Array('i', [1, 2, 3])

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

import multiprocessing
import time


def job(v, num, lock):
    lock.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value)
    lock.release()


def multicore():
    # 加进程锁，让有序使用共享内存
    lock = multiprocessing.Lock()
    v = multiprocessing.Value('i', 0)
    p1 = multiprocessing.Process(target=job, args=(v, 1, lock))
    p2 = multiprocessing.Process(target=job, args=(v, 3, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('All done!')


if __name__ == '__main__':
    multicore()
