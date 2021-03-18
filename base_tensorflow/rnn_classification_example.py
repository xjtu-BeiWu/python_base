# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/15 21:33
# File: rnn_classification_example.py
# IDE: PyCharm

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.ops.rnn import dynamic_rnn
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
    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden_units)
    init_state = lstm_cell.zero_state(batch_size, dtype=tf.float32)
    outputs, states = dynamic_rnn(lstm_cell, x_in, initial_state=init_state)
    outputs = tf.unstack(tf.transpose(outputs, [1, 0, 2]))
    results = tf.matmul(outputs[-1], weights['out']) + biases['out']
    return results


prediction = rnn(x, w, b)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
train_op = tf.train.AdamOptimizer(lr).minimize(cost)

correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    step = 0

    while step * batch_size < training_iters:
        batch_x_input, batch_y_input = mnist.train.next_batch(batch_size)
        batch_xs = batch_x_input.reshape([batch_size, n_steps, n_inputs])
        sess.run([train_op], feed_dict={
            x: batch_xs,
            y: batch_y_input,
        })
        if step % 20 == 0:
            print(sess.run(accuracy, feed_dict={
                x: batch_xs,
                y: batch_y_input,
            }))
        step += 1
