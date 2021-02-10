# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/9 10:50
# File: def_func.py
# IDE: PyCharm

import numpy as np


# *表示是可变参数，可迭代的对象。
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade = total_grade + grade
    print(name + ' total grade is ' + str(total_grade))


# **表示关键词参数，参数在函数内部自动封装成一个字典(dict).
def portrait(name, **kwargs):
    print('My name is: ', name)
    for k, v in kwargs.items():
        print(k, v)


# 关于局部变量和全局变量
def fun():
    global a  # 使用之前定义的全局变量a
    a = 2020
    return a + 1


if __name__ == '__main__':
    portrait('Bella', age=27, country='China', education='doctor')
    report('Bella', 100, 100, 100)
    a = None
    print(a)
    fun()
    print(a)
