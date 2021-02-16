# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/16 21:12
# File: class_init.py.py
# IDE: PyCharm

class Calculator:
    name = 'Good Calculator'
    price = 100
    def __init__(self, name, price, height=10, width=14, weight=15):
        self.name = name
        self.price = price
        self.h = height
        self.wi = width
        self.we = weight

    def add(self, x, y):
        print(self.name)
        result = x+y
        print(result)
    def minus(self, x, y):
        result = x-y
        print(result)
    def times(self, x, y):
        print(x*y)
    def divide(self, x, y):
        print(x/y)


if __name__ == '__main__':
    # cal = Calculator()
    # cal.add(10, 20)
    # cal.minus(10, 20)
    cal = Calculator('bad calculator', 18)
    print(cal.name)
    print(str(cal.h))
    print(str(cal.wi)+','+str(cal.we))
