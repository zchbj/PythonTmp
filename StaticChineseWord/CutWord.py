#!/usr/bin/python
# -*- coding: UTF-8 -*-

import jieba as jb
import os
import sys

TEST_STRING = '中文分词测试，不知道准不准确, 百度搜索不如谷歌, 工商银行总部在北京'

word_list = jb.cut(TEST_STRING, cut_all=True)
print 'Full Mode: %s' % ' '.join(word_list)

word_list = jb.cut(TEST_STRING, cut_all=False)
print 'Defual Mode: %s' % ' '.join(word_list)

word_list = jb.cut_for_search(TEST_STRING)
print 'Search Mode: %s' % ' '.join(word_list)

 