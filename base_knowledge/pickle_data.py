# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/17 17:07
# File: pickle_data.py
# IDE: PyCharm

import pickle

a_dict = {'a': 1, 'b': 2, 3: ['hello', 'world']}

# pickle a variable to a file
file = open('../test_file/pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

# reload a file to a variable
with open('../test_file/pickle_example.pickle', 'rb') as f:
    a_dict_copy = pickle.load(f)

print(a_dict_copy)

# reload a file with exception
try:
    file = open('../test_file/pickle_example_copy.pickle', 'ab')
except Exception as e:
    print(e)
    response = input('Do you want to creat a new file for pickle: ')
    if response == 'y':
        file = open('../test_file/pickle_example_copy.pickle', 'wb')
    else:
        pass

else:
    pickle.dump(a_dict, file)
    file.close()
