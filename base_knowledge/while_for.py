condition = 1
while condition < 10:
    print(condition)
    condition += 1

example_list = [0,1,2,3,4,5,6,7,8,9,10]
for i in example_list:
    print(i)
    print("inner of for")
print("outer of for")

# for tuple
tup = ('python', 2.7, 64)
for i in tup:
    print(i)

# for dictionary
dic = {}
dic['lan'] = 'python'
dic['version'] = 2.7
dic['platform'] = 64
for key in dic:
    print(key, dic[key])

# for set
s = set(['python', 'python2', 'python3','python'])
for item in s:
    print(item)
