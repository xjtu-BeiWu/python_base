# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/18 20:26
# File: threading_example.py
# IDE: PyCharm

# 多线程threading：处理一堆数据，将这堆数据分成好几段，然后一段的数据放在一个线程中，多个线程同时开始可以节省运算的时间。
import threading

def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job)  # 添加线程
    thread.start()  # 启动线程

    # 获取已经激活的线程数量
    count = threading.active_count()
    print(str(count))

    # 查看所有线程信息: 一般是<_MainThread(...)>带多个<Thread(...)>
    print(threading.enumerate())

    # 获取正在运行的线程信息
    print(threading.current_thread())

if __name__ == '__main__':
    main()

