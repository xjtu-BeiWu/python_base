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