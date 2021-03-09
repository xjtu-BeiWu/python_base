# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/9 21:49
# File: classification.py
# IDE: PyCharm

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from nn_example import add_layer

# 全局取消证书验证
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)

x_input = tf.placeholder(tf.float32, [None, 784])
y_input = tf.placeholder(tf.float32, [None, 10])
prediction = add_layer(x_input, 784, 10, 1, activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_input*tf.log(prediction), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.Session()
sess.run(tf.global_variables_initializer())


def compute_accuracy(value_x, value_y):
    global prediction
    y_pre = sess.run(prediction, feed_dict={x_input: value_x})
    correct_prediction = tf.equal(tf.argmax(y_pre, 1), tf.argmax(value_y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    result = sess.run(accuracy, feed_dict={x_input: value_x, y_input: value_y})
    return result


for i in range(1000):
    batch_x_input, batch_y_input = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x_input: batch_x_input, y_input: batch_y_input})
    if i % 50 == 0:
        print(compute_accuracy(mnist.test.images, mnist.test.labels))
