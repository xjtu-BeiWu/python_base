# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/11 22:34
# File: test.py
# IDE: PyCharm

import tensorflow as tf
# import numpy as np

# w = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name='weights')
# b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name='biases')
#
# saver = tf.train.Saver()
# with tf.Session() as sess:
#     saver.restore(sess, '')
#     print('weights:', sess.run(w))
#     print('biases:', sess.run(b))

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('../my_net/save_net_cnn_name.ckpt.meta')
    saver.restore(sess, '../my_net/save_net_cnn_name.ckpt')
    # print(sess.run(''))
    variable_names = [v.name for v in tf.trainable_variables()]
    for v in tf.global_variables():
        variable_names.append(v.name)
    values = sess.run(variable_names)
    for k, v in zip(variable_names, values):
        # if k.find('encode') != -1:
        print('Variable: ', k)
        print('Shape: ', v.shape)
        print(v)
    graph = tf.compat.v1.get_default_graph()
    all_ops = graph.get_operations()
    for el in all_ops:
        print(el.name)
    # X = graph.get_operation_by_name('keep_prob').outputs[0]
    # print(sess.run(graph.get_operation_by_name('keep_prob')))
    # print(sess.run(graph.get_operation_by_name('w1')))
