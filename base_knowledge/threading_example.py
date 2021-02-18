# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/18 20:26
# File: threading_example.py
# IDE: PyCharm

# 多线程threading：处理一堆数据，将这堆数据分成好几段，然后一段的数据放在一个线程中，多个线程同时开始可以节省运算的时间。
import threading
import time

from queue import Queue


def thread_job():
    print('This is a thread of %s' % threading.current_thread())


def t1():
    print('t1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('t1 finish\n')


def t2():
    print('t2 start\n')
    print('t2 finish\n')


# 主线程
def main():
    # thread = threading.Thread(target=thread_job)  # 添加线程
    # thread.start()  # 启动线程
    #
    # # 获取已经激活的线程数量
    # count = threading.active_count()
    # print(str(count))
    #
    # # 查看所有线程信息: 一般是<_MainThread(...)>带多个<Thread(...)>
    # print(threading.enumerate())
    #
    # # 获取正在运行的线程信息
    # print(threading.current_thread())
    thread1 = threading.Thread(target=t1, name='t1')  # t1后面没有括号，它只是一个索引
    thread2 = threading.Thread(target=t2, name='t2')
    thread1.start()
    thread2.start()
    thread1.join()  # join控制多个线程的执行顺序，如果加了join会让线程执行完在执行主线程接下来的语句
    thread2.join()
    print('all threads done!\n')


# 多线程返回值问题：多线程中是没有返回值的，这时候需要引入队列保存结果，在线程执行完成后，从队列中获取存储结果
def job(d, q):
    for i in range(len(d)):
        d[i] = d[i] ** 2
    q.put(d)

def multithreading(data):
    q = Queue()
    threads = []
    for i in range(len(data)):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(len(data)):
        results.append(q.get())
    return results


if __name__ == '__main__':
    # main()
    data = [[1, 2, 3], [2, 3, 4], [4, 5, 6]]
    re = multithreading(data)
    print(re)