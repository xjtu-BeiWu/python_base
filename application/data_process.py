# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2019/01/20 21:54
# File: data_process.py
# IDE: PyCharm

# from bert_serving.client import BertClient
import numpy as np
import re
import time
import os


# np.set_printoptions(suppress=True)
# bc = BertClient(ip='localhost', check_version=False, check_length=False)


# def test():
# vec = bc.encode(['hello world', 'hello', 'world'])
# print(vec)

#
# def write_file(outsid):
#     output = open('', 'w')
#     output.write(outsid)
#     output.write("\n")


# 读取文本的前10行
def read():
    infile = open('../data/manifesto/61320_200411.txt')
    i = 0
    for line in infile:
        if i in range(10):
            print(line)
            print('---------------------------------')
            i += 1
    infile.close()


# 递归遍历文件中txt文件
def get_file_list(foot_path, file_list):
    # newDir = footPath
    if os.path.isfile(foot_path):
        file_list.append(foot_path)
    elif os.path.isdir(foot_path):
        for s in os.listdir(foot_path):
            new_dir = os.path.join(foot_path, s)
            get_file_list(new_dir, file_list)
    return file_list


# 生成tag文件
def gen_tag(foot_dir, out_file_dir, out_tag_dir):
    if os.path.isdir(foot_dir):
        for s in os.listdir(foot_dir):
            out_file_path = os.path.join(out_file_dir, s)
            file_w = open(out_file_path, 'a+')
            out_tag_path = os.path.join(out_tag_dir, s)
            tag_w = open(out_tag_path, 'a+')
            file_path_dir = os.path.join(foot_dir, s)
            file_list = os.listdir(file_path_dir)
            for name in file_list:
                file_path = os.path.join(file_path_dir, name)
                f = open(file_path, 'r')
                for line in f.readlines():
                    file_w.write(line+'\n')
                    tag_w.write(name.replace('.txt','')+'\n')
                f.close()
            file_w.flush()
            file_w.close()
            tag_w.flush()
            tag_w.close()

# 标签转换
def tag_trans(dir):
    pass

# 将文本转换成bert向量 300d
# def read_and_write():
#     infile = open('../data/manifesto/61320_200411.txt')
#     output_file = open('../data/manifesto_bert/61320_200411.txt', 'a+')
#     n = 0
#     m = [0 for i in range(30)]
#     j = 0
#     for line in infile:
#         if line != '==========':
#             if line != '\n':
#                 vec = bc.encode([line])
#                 s = str(vec).replace('\n', '').strip('[[').strip(']]')
#                 # s = str(vec).replace('\n', '').replace(' ', '').strip('[[').strip(']]')
#                 # s = re.compile(' ').sub('', str(vec).replace('\n', '').strip('[[').strip(']]'))
#                 output_file.write(s)
#                 output_file.write('\n')
#                 n = n + 1
#             else:
#                 m[j] = n
#                 # print(line)
#                 # print('null-line is:' + str(n))
#                 j = j + 1
#         else:
#             output_file.write('\n')
#     infile.close()
#     output_file.flush()
#     output_file.close()


# 去除各个数字之间的“,”
def reprocess():
    infile = open('../data/manifesto_bert/61320_200411.txt')
    output = open('../data/manifesto_bert_r/61320_200411.txt', 'a+')
    for line in infile:
        if line != '\n':
            s = line.replace(', ', ' ')
            output.write(s)
    infile.close()
    output.close()


# 将生成的txt文件转换成.npy文件
def extract_data(filename, num):
    """Extract the images into a 4D tensor [image index, y, x, channels]."""
    print('Extracting', filename)
    data = np.loadtxt(filename)  # 从文件读取数据，存为numpy数组
    data = np.frombuffer(data).astype(np.float32)  # 改变数组元素变为float32类型
    data = data.reshape(num, 768)  # 所有元素
    return data


if __name__ == "__main__":
    print('start......')
    # read_and_write()

    # reprocess()

    # # Extract it into numpy arrays.
    # start_time = time.time()
    # infile_path = '../data/manifesto_bert_r/61320_200411.txt'
    # outfile_path = '../data/manifesto_bert_npy/61320_200411.npy'
    # num_sentence = 1033394
    # features = extract_data(infile_path, num_sentence)
    # features_file = np.save(outfile_path, features)
    # elapsed_time = time.time() - start_time
    # print(elapsed_time, 's')
    #
    # # read()
    #
    # # test()

    # list = get_file_list('../data/test', [])
    # print(len(list))
    # for e in list:
    #     print(e)

    gen_tag('../data/test', '../data/gen/new_file', '../data/gen/tag')

    print('end.......')
