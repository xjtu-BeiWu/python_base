# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/8 15:18
# File: vari_example.py
# IDE: PyCharm

import tensorflow as tf

state = tf.Variable(0, name='counter')
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 如果定义Variable就一定要initialize
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))