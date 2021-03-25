# -*- coding: utf-8 -*-
# Author: bellawu
# Date: 2019/2/16 21:12
# File: fts_model.py
# IDE: PyCharm

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
# from tensorflow.python.ops.rnn import dynamic_rnn
from tensorflow.python.ops.rnn import bidirectional_dynamic_rnn
from tensorflow.contrib.crf import crf_log_likelihood, crf_decode
tf.set_random_seed(1)

mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)

lr = 0.001
training_iters = 100000
batch_size = 128
n_inputs = 28
n_steps = 28
n_hidden_units = 128
max_seq_len = 100
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


def fts_model(x_inputs, weights, biases):
    # 句子向量生成
    # x_inputs(128 batch, 28 steps, 28 inputs)-->(128*28, 28 inputs)
    # -1表示根据n_inputs大小计算出数组的另外一个shape的属性值，使其符合原来的维度
    x_inputs = tf.reshape(x_inputs, [-1, n_inputs])
    # x_in(128 batch * 28 steps, 128 hidden) =
    # x_inputs(128*28, 28) * weights(28 inputs, 128 hidden) + biases(128 hidden, )
    x_in = tf.matmul(x_inputs, weights['in']) + biases['in']
    # x_in(128 batch, 28 step, 128 hidden)
    x_in = tf.reshape(x_in, [-1, n_steps, n_hidden_units])
    cell_fw = tf.contrib.rnn.LSTMCell(n_hidden_units)
    cell_bw = tf.contrib.rnn.LSTMCell(n_hidden_units)
    (outputs, output_states) = bidirectional_dynamic_rnn(cell_fw, cell_bw, x_in, n_steps)
    output_fw, output_bw = outputs
    output_sen = tf.concat([output_fw, output_bw], axis=-1)

    # NER模型转换

    w_crf = tf.get_variable('w_crf', [2 * n_hidden_units, n_classes])
    matricized_output = tf.reshape(output_sen, [-1, 2 * n_hidden_units])
    matricized_unary_scores = tf.matmul(matricized_output, w_crf)
    unary_scores = tf.reshape(matricized_unary_scores, [batch_size, max_seq_len, n_classes])
    return unary_scores

prediction = fts_model(x, w, b)
# cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
# train_op = tf.train.AdamOptimizer(lr).minimize(cost)
# correct_prediction = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
# accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
log_likelihood, transition_params = crf_log_likelihood(prediction, y, n_steps)
loss = tf.reduce_mean(-log_likelihood)
decode_tags, best_score = crf_decode(prediction, transition_params, n_steps)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    mask = (np.expand_dims(np.arange(n_inputs), axis=0)<np.expand_dims(n_steps,axis=1))
    step = 0
    total_labels = np.sum()
