# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/16 20:31
# File: read_write_file.py
# IDE: PyCharm

def read_write(file_path):
    append_text = '\nThis is appended line.'
    my_file = open(file_path, 'a+')
    my_file.write(append_text)
    my_file.close()

def read(file_path):
    file = open(file_path,'r')
    content = file.readlines()
    print(content)
    file.close()

file_path = '/test_file/my_file.txt'
read_write(file_path)
read(file_path)

