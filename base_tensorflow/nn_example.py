# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/8 16:32
# File: nn_example.py
# IDE: PyCharm

import tensorflow as tf
import numpy as np
# import matplotlib.pyplot as plt


def add_layer(inputs, in_size, out_size, n_layer, activation_function=None):
    layer_name = 'layer%s' % n_layer
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            weights = tf.Variable(tf.random_normal([in_size, out_size]), name='weight')
            tf.summary.histogram(layer_name+'/weights', weights)

        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='biases')
            tf.summary.histogram(layer_name+'/biases', biases)

        with tf.name_scope('wx_plus_b'):
            wx_plus_b = tf.add(tf.matmul(inputs, weights), biases)

        if activation_function is None:
            outputs = wx_plus_b
        else:
            outputs = activation_function(wx_plus_b,)

        tf.summary.histogram(layer_name+'/outputs', outputs)

    return outputs


x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
y_data = np.square(x_data) - 0.5 + noise

with tf.name_scope('inputs'):
    x_input = tf.placeholder(tf.float32, [None, 1], name='x_in')
    y_output = tf.placeholder(tf.float32, [None, 1], name='y_in')

# l1 = add_layer(x_input, 1, 10, activation_function=tf.nn.relu)
l1 = add_layer(x_input, 1, 10, n_layer=1, activation_function=tf.nn.relu)
# prediction = add_layer(l1, 10, 1, activation_function=None)
prediction = add_layer(l1, 10, 1, n_layer=2, activation_function=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(y_output-prediction), reduction_indices=[1]))
    tf.summary.scalar('loss', loss)

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter('../tb_logs/test_log1/', sess.graph)
    sess.run(init)

    # # 散点图显示真实数据关系
    # # 新建绘图窗口
    # fig = plt.figure()
    # # 设置画布大小为一行一列一块
    # ax = fig.add_subplot(1, 1, 1)
    # ax.scatter(x_data, y_data)
    # # show以后不暂停
    # plt.ion()
    # # 显示图像
    # plt.show()

    for i in range(1000):
        sess.run(train_step, feed_dict={x_input: x_data, y_output: y_data})
        # if i % 50 == 0:
        #     # noinspection PyBroadException
        #     try:
        #         # 新增一条线后删除原来的线
        #         ax.lines.remove(lines[0])
        #     except Exception:
        #         pass
        #     prediction_value = sess.run(prediction, feed_dict={x_input: x_data})
        #     # 可视化线条
        #     lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        #     # 每次循环暂停1s
        #     plt.pause(1)
        #     # print(sess.run(loss, feed_dict={x_input: x_data, y_output: y_data}))
        if i % 50 == 0:
            rs = sess.run(merged, feed_dict={x_input: x_data, y_output: y_data})
            writer.add_summary(rs, i)
