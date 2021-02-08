# -*- coding: utf-8 -*-

x = 3
y = 2
z = 0
if x > y:
    print("x is greater than y.")
else:
    print("x is less than y.")

worked = False
# 通过行内表达式完成类似三目操作符
result = 'done' if worked else 'not yet'
print(result)

if x > 1:
    print('x>1')
elif x < 1:
    print('x<1')
else:
    print('x=1')
