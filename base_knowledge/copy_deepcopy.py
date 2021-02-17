# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/17 15:32
# File: copy_deepcopy.py
# IDE: PyCharm

import copy

a = [1, 2, 3]
b = a
b[1] = 20
# 赋值后两者的id相同，改变b值也会导致a的值发生改变
# print(id(a) == id(b))
# print(id(a))
# print(b)
# print(a)

# shallow copy
# c = copy.copy(a)  # 拷贝了a的外围对象本身，内部元素只是拷贝了一个引用
# print(id(c))
# print(id(a) == id(c))
# print(id(a[2]) == id(c[2]))
# a[2] = 1234
# print(a)
# print(c)
a1 = [1, 2, [3, 4]]
c1=copy.copy(a1)
print(id(a1) == id(c1))
print(id(a1[2]) == id(c1[2]))
a1[2][1] = 10
print(a1)
print(c1)  # 因为是浅拷贝，那么c1的内部元素[]列表的值会因为a1的值的改变而改变

# deep copy
# d = copy.deepcopy(a)  # 不仅拷贝了a的外围对象本身，也拷贝了内部元素
# print(id(a) == id(d))
# print(id(a[2]) == id(d[2]))
# print(id(a))
# print(id(d))
# d[1] = 23456
# print(a)
# print(d)
d1=copy.deepcopy(a1)
print(id(a1) == id(d1))
print(id(a1[2]) == id(d1[2]))
a1[2][1] = 12
print(a1)
print(d1)  # 因为是深拷贝，那么d1的内部元素[]列表的值不会因为a1的值的改变而改变