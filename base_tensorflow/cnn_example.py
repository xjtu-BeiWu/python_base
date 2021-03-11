# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/10 21:20
# File: cnn_example.py
# IDE: PyCharm

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)


def compute_accuracy_prob(value_x, value_y):
    global prediction
    y_pre = sess.run(prediction, feed_dict={x_input: value_x, keep_prob: 1})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(value_y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={x_input: value_x, y_input: value_y, keep_prob: 1})
    return result


def weight_variable(shape):
    # truncated_normal 截断的产生正态分布的随机数，即随机数与均值的差值若大于两倍的标准差，则重新生成。
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, w):
    return tf.nn.conv2d(x, w, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    # return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')  # 0.969
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')  # 0.969


keep_prob = tf.placeholder(tf.float32)
x_input = tf.placeholder(tf.float32, [None, 784])
y_input = tf.placeholder(tf.float32, [None, 10])

x_image = tf.reshape(x_input, [-1, 28, 28, 1])

# 构建第一层卷积
# 卷积核大小为5*5，32个feature map
w_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, w_conv1)+b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# 构建第二层卷积
w_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, w_conv2)+b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 构建全连接层
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
w_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, w_fc1)+b_fc1)
# 加入dropout
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
w_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, w_fc2)+b_fc2)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_input*tf.log(prediction), reduction_indices=[1]))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch_x_input, batch_y_input = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x_input: batch_x_input, y_input: batch_y_input, keep_prob: 0.5})
    if i % 50 == 0:
        print(compute_accuracy_prob(mnist.test.images[:1000], mnist.test.labels[:1000]))
