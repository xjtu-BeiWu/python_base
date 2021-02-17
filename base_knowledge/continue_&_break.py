# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/17 10:51
# File: continue_&_break.py
# IDE: PyCharm

while True:
    a = input('input something: ')
    if a=='1':
        break # break在循环语句中直接结束循环
    else:
        pass
    print('still in while')

print('finish iteration')

while True:
    b = input('input something: ')
    if b=='1':
        continue # continue在循环语句中，不会执行else后面的只是跳出当前循环进入下一次循环
    else:
        pass
    print('still in while')


print('finish iteration')