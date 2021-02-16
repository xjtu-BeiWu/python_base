# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/16 21:23
# File: input_expansion.py
# IDE: PyCharm

a_input = input('please input a word: ')
print('this word is:', a_input)

s = input('please input your name and score: \n')
name, score = s.split()
score = int(score)
print(name)
if score>=90:
    print('Congratulation, you get an A!')
elif score>=80:
    print('You get a B.')
elif score>=70:
    print('You get a C.')
elif score>=60:
    print('You get a D.')
else:
    print('Sorry, you are failed.')