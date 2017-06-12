#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import jieba as jb


def read_file(file_name):
    with open(file_name, 'r') as f:
        file_data_list = f.readlines()
    return file_data_list

def cut_file(file_data_list):
    cutted_data_list = []
    for line_data in file_data_list:
        word_list = jb.cut(line_data, cut_all = False)
        cutted_data_list.append(' '.join(word_list).encode('utf-8'))

    return cutted_data_list

def write_file(file_data_list, cutted_file_name):
    with open(cutted_file_name, 'wb') as f:
        f.writelines(file_data_list)
    return cutted_file_name

def read_file_name():
    print 'Please input filename or Enter to exit:'
    input_str = raw_input()
    return input_str

while True:
    input_str = read_file_name()
    if input_str == '':
        print 'Nothing be done!'
        exit(0)
    else:
        if not os.path.exists(input_str):
            print 'Can\'t find the file %s' % input_str
        else:
            file_name = input_str
            file_data = read_file(file_name)
            cutted_file_data = cut_file(file_data)
            cutted_file_name = write_file(cutted_file_data, file_name + '.cutted')
            print 'Cut file %s done. New file is %s .' % (file_name, cutted_file_name)



