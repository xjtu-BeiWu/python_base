# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/16 21:37
# File: data_type.py
# IDE: PyCharm

# tuple
a_tuple = 1, 2, 3, 4, 5, 6
another_tuple = (1, 2, 3, 4, 5, 6)
for index in range(len(a_tuple)):
    print('index = ', index, 'number in tuple = ', a_tuple[index])

# list
a_list = [1, 2, 3, 4, 5, 6]
for index in range(len(a_list)):
    print('index = ', index, 'number in list = ', a_list[index])
for content in a_list:
    print(content)
# about insertion and deletion for list
a_list.remove(2)
print(a_list)
a_list.append(0)
print(a_list)
a_list.insert(1,-2)
print(a_list)
# about list indexing and sorting
print(a_list[1:])
print(a_list[-3:])
print(a_list.index(-2))
print(a_list.count(1))
a_list.sort()
print(a_list)
a_list.sort(reverse=True)
print(a_list)

# 2-dimension list
multi_dim_list = [[1,2,3],
                  [2,3,4],
                  [3,4,5]]
print(multi_dim_list[0][1])

# dictionary:key value
# 在同一字典中并不需要所有的key和value有相同的形式
d1 = {'apple':1, 'pear':2, 'orange':3}
d2 = {1:'a', 2:'b', 3:'c'}
d3 = {1:'a', 'b':2, 'c':3}
print(d1['apple'])
del d1['apple']
print(d1)
d1['b'] = 20
print(d1) # 字典元素并不会按照规律打印出来，字典是一个无序的容器。
