# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/8 15:27
# File: placeholder_example.py
# IDE: PyCharm

import tensorflow as tf

# placeholder需要定义类型，并且一般与feed_dict{}配套使用
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)
output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [7.], input2: [2.]}))
