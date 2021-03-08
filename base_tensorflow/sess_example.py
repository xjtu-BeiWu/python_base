# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/8 14:56
# File: sess_example.py
# IDE: PyCharm

import tensorflow as tf

matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])
product = tf.matmul(matrix1, matrix2)

# way1 to use Session
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

# way2 to use Session
with tf.Session() as sess:
    result_ = sess.run(product)
    print(result_)