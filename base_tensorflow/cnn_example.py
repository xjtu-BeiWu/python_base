# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/3/10 21:20
# File: cnn_example.py
# IDE: PyCharm

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data


mnist = input_data.read_data_sets('MNIST_DATA', one_hot=True)


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
