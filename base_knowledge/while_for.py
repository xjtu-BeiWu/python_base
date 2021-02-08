# -*- coding: utf-8 -*-

# condition = 1
# while condition < 10:
#     print(condition)
#     condition += 1
#
# example_list = [0,1,2,3,4,5,6,7,8,9,10]
# for i in example_list:
#     print(i)
#     print("inner of for")
# print("outer of for")

# for tuple
# tup = ('python', 2.7, 64)
# for i in tup:
#     print(i)

# for dictionary
# dic = {}
# dic['lan'] = 'python'
# dic['version'] = 2.7
# dic['platform'] = 64
# for key in dic:
#     print(key, dic[key])

# for set
# s = set(['python', 'python2', 'python3','python'])
# for item in s:
#     print(item)

# for iter
class Fib(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):  # 在python3.0中应该使用__next__
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()  # 手动设置异常：raise [exceptionName [(reason)]]


# for generation
def fib(max):
    a, b = 0, 1
    while max:
        r = b
        a, b = b, a+b
        max -= 1
        yield r


if __name__ == '__main__':
    for i in Fib(5):
        print(i)
    for j in fib(5):
        print j

