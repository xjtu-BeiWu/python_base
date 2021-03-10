# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/10 16:15
# File: dropout_example.py
# IDE: PyCharm

import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

# from base_tensorflow.nn_example import add_layer

digits = load_digits()
x = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)


def add_layer(inputs, in_size, out_size, layer_name, activation_function=None):
    weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size])+0.1,)
    wx_plus_b = tf.add(tf.matmul(inputs, weights), biases)
    # 增加dropout层，keep_prob为保留概率，保留结果所占比例。
    wx_plus_b = tf.nn.dropout(wx_plus_b, keep_prob)
    if activation_function is None:
        outputs = wx_plus_b
    else:
        outputs = activation_function(wx_plus_b, )
    tf.summary.histogram(layer_name + '/outputs', outputs)
    return outputs


keep_prob = tf.placeholder(tf.float32)
x_input = tf.placeholder(tf.float32, [None, 64])
y_input = tf.placeholder(tf.float32, [None, 10])

l1 = add_layer(x_input, 64, 50, 'l1', activation_function=tf.nn.tanh)
prediction = add_layer(l1, 50, 10, 'l2', activation_function=tf.nn.softmax)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_input * tf.log(prediction), reduction_indices=[1]))

tf.summary.scalar('loss', cross_entropy)
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.Session()
merged = tf.summary.merge_all()

train_writer = tf.summary.FileWriter('../tb_logs/train', sess.graph)
test_writer = tf.summary.FileWriter('../tb_logs/test', sess.graph)

sess.run(tf.global_variables_initializer())
for i in range(500):
    sess.run(train_step, feed_dict={x_input: x_train, y_input: y_train, keep_prob: 0.5})
    if i % 50 == 0:
        train_result = sess.run(merged, feed_dict={x_input: x_train, y_input: y_train, keep_prob: 1})
        test_result = sess.run(merged, feed_dict={x_input: x_test, y_input: y_test, keep_prob: 1})
        train_writer.add_summary(train_result, i)
        test_writer.add_summary(test_result, i)
print('Everything is finished!')
