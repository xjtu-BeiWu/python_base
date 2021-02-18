# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/18 20:26
# File: threading_example.py
# IDE: PyCharm

# 多线程threading：处理一堆数据，将这堆数据分成好几段，然后一段的数据放在一个线程中，多个线程同时开始可以节省运算的时间。
import threading
import time


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
    thread1 = threading.Thread(target=t1, name='t1')
    thread2 = threading.Thread(target=t2, name='t2')
    thread1.start()
    thread2.start()
    thread1.join()  # join控制多个线程的执行顺序，如果加了join会让线程执行完在执行主线程接下来的语句
    thread2.join()
    print('all threads done!\n')


if __name__ == '__main__':
    main()
