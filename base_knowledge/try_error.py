# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/17 11:06
# File: try_error.py
# IDE: PyCharm


try:
    file = open('../test_file/test.txt','r+')
except Exception as e:
    print(e)
    response = input('Do you want to create a new file: ')
    if response=='y':
        file = open('../test_file/test.txt', 'w')
    else:
        pass

else:
    file.write('error process successful')
    file.close()
