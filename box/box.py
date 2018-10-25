#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


def get_array(industries, max_len, padding_left):
    industries.sort(reverse=True)  # 数列倒排序
    # 至少需要N+1行,N= 总和/行长度
    row_num = int(math.ceil((sum(industries) + len(industries)*padding_left)*1.0 / (max_len + padding_left)))
    rows = [[] for n in range(row_num)]
    row_index = 0  # 第一行开始插入
    next_value_index = 0  # 第一次默认从第一个位置开始
    while next_value_index < len(industries):
        rows[row_index].append(industries[next_value_index])  # 把获取到符合条件的值插入到最短行的队尾
        industries.pop(next_value_index)  # 待处理队列中删除符合条件的值

        # 进入下一轮
        row_index = get_sum_min_row_index(rows, padding_left)  # 获取下个空余最多的行
        next_max_value = max_len - sum(rows[row_index]) - len(rows[row_index])*padding_left  # 计算此行剩余可用长度
        next_value_index = get_first_value_index(industries, next_max_value)  # 从行业长度列表中获取最大数字

    # 多余的数列不为空，递归调用求解
    if len(industries) > 0:
        sub_rows = get_array(industries, max_len, padding_left)
        if len(sub_rows) > 0:
            rows.extend(sub_rows)  # 迭代结果追加到本次计算结果后面

    return rows


# 返回列表中小于目标值的第一数字的位置
def get_first_value_index(industries, max_value):
    return sum([1 if i > max_value else 0 for i in industries])


# 返回行数组中，行数字和最小的数组编号
def get_sum_min_row_index(rows, padding_left):
    rows_sum = [sum(nums) + len(nums)*padding_left for nums in rows]
    return rows_sum.index(min(rows_sum))


# 数列进行行组合处理过程
def magic(industries, column_max_len=30, padding_left=2):
    if max(industries) > column_max_len:
        print "单个长度超过行长度限制"
        return
    industries.sort(reverse=True)
    result = get_array(industries[:], column_max_len, padding_left)
    result.sort(key=lambda a: sum(a)+len(a)*2, reverse=True)  # 根据结果的行的长度倒排序

    print '排序后列表：%s' % industries
    print '列表之和：%d; 行长度限制：%d; 间距：%d' % (sum(industries), column_max_len, padding_left)
    print '结果如下: %s' % result
    print '1234567890'*8
    for rowIndex in range(len(result)):
        x = ''
        for colIndex in range(len(result[rowIndex])):
            x = x + "X"*result[rowIndex][colIndex] + "  "
        print x
    return


# 主函数
def main():
    industries = [9, 3, 3, 16, 3, 6, 11, 6, 15, 3, 4, 8, 10, 13, 13, 2, 7, 9, 14, 4]
    magic(industries)
    industries = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
    magic(industries)
    industries = [16, 16, 16, 16, 16, 16, 13, 13, 13, 13, 13, 13]
    magic(industries)
    industries = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    magic(industries)
    industries = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    magic(industries)
    industries = [2, 18, 4, 8, 12, 23, 13, 1, 2, 4, 6, 7, 8, 9, 10, 2, 2, 18, 4, 8, 12, 23, 13, 1, 2, 4, 6, 7, 8, 9]
    magic(industries)
    return


main()