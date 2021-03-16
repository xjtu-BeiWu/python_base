# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/15 21:33
# File: rnn_classification_example.py
# IDE: PyCharm

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
tf.set_random_seed(1)

mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)

lr = 0.001
training_iters = 100000
batch_size = 128
n_inputs = 28
n_steps = 28
n_hidden_units = 128
n_classes = 10

x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_classes])

w = {
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
}
b = {
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
}


def rnn(x_inputs, weights, biases):
    # x_inputs(128 batch, 28 steps, 28 inputs)-->(128*28, 28 inputs)
    # -1表示根据n_inputs大小计算出数组的另外一个shape的属性值，使其符合原来的维度
    x_inputs = tf.reshape(x_inputs, [-1, n_inputs])
    # x_in(128 batch * 28 steps, 128 hidden) =
    # x_inputs(128*28, 28) * weights(28 inputs, 128 hidden) + biases(128 hidden, )
    x_in = tf.matmul(x_inputs, weights['in']) + biases['in']
    # x_in(128 batch, 28 step, 128 hidden)
    x_in = tf.reshape(x_in, [-1, n_steps, n_hidden_units])
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units, forget_bias=1.0, state_is_tuple=True)
    _init_state = lstm_cell.zero_state(batch_size, dtype=tf.float32)
    outputs, states = tf.nn.dynamic_rnn(lstm_cell, x_in, initial_state=_init_state, time_major=False)
    results = tf.matmul(states[1], weights['out']) + biases['out']
    return results
