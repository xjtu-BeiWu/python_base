# -*- coding: utf-8 -*-  
# Author: BellaWu
# Date: 2021/2/17 11:25
# File: zip_lambda_map.py
# IDE: PyCharm


# zip: 接受多个任意序列为参数，合并后返回一个tuple列表
a = [1,2,3]
b = [4,5,6]
ab = zip(a,b)
print(list(ab))
for i, j in zip(a,b):
    print(i/2, j*2)

# lambda：简单的函数，实现简化代码的功能
func = lambda x, y: x+y
x = int(input('Please input a number x = '))
y = int(input('Please input another number y = '))
print(func(x,y))

# map：把函数和参数绑定在一起
print(list(map(func, [1,2], [3,4])))
