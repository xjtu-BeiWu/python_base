# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/17 20:30
# File: set_basis.py
# IDE: PyCharm

# set最主要的功能是寻找句子或者list中不同的元素
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
print(set(char_list))

a_sentence = 'Welcome to Bella\'s python world!'
print(set(a_sentence))

unique_list = set(char_list)
unique_list.add('e')
print(unique_list)
unique_list.remove('a')
print(unique_list)
unique_list.discard('b')
print(unique_list)
unique_list.clear()
print(unique_list)

unique_list = set(char_list)
print(unique_list)
print(unique_list.difference({'a', 'e'}))
print(unique_list.intersection({'a', 'e'}))