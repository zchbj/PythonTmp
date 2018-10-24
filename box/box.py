#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


def getArray(list, maxLen, paddingLeft):
    nextList = [] #多余的数列，需要进入迭代求解
    subResultArray = [] #从迭代计算中获取到的组合结果
    list.sort(reverse = True) #数列倒排序
    rowNum = int(math.ceil((sum(list) + len(list)*paddingLeft )*1.0 / (maxLen+paddingLeft))) #至少需要N+1行,N= 总和/行长度
    resultArray = [[] for n in range(rowNum)]
    rowIndex = 0 #第一行开始插入
    nextValueIndex = 0 # 第一次默认从第一个位置开始
    while (nextValueIndex) < len(list):
        # 把获取到符合条件的值插入到最短行的队尾
        resultArray[rowIndex].append(list[nextValueIndex])

        # 如果取值有跳跃，把跳跃过去的值放入迭代计算列表
        if nextValueIndex > 0:
            nextList.append(list[0:nextValueIndex + 1])
        # 截取list，进入下一轮
        del list[0:nextValueIndex + 1]
        rowIndex = getSumMinRowIndex(resultArray)
        # 可用长度=最大长度-已用长度-数字个数*间隔长度
        nextMaxValue = maxLen - sum(resultArray[rowIndex]) - len(resultArray[rowIndex]) * paddingLeft
        nextValueIndex = getFirstValueIndex(list, nextMaxValue)

    nextList.extend(list) # 没处理完的列表也放入到下次迭代中去
    if len(nextList) > 0:
        # 多余的数列不为空，递归调用求解
        subResultArray = getArray(nextList, maxLen, paddingLeft)

    #返回本次解和迭代解的合集
    if len(subResultArray)>0:
        resultArray.extend(subResultArray)

    return resultArray


#返回列表中小于目标值的第一数字的位置
def getFirstValueIndex(list, maxValue):
    return sum([1 if i > maxValue else 0 for i in list])

#返回行数组中，行数字和最小的数组编号
def getSumMinRowIndex(rowList):
    rowSumList = [sum(subList) for subList in rowList]
    return rowSumList.index(min(rowSumList))


# 数列进行行组合处理过程
def doList(industryLenList):
    columnMaxLen = 30
    paddingLeft =2
    industryLenList.sort(reverse=True)
    rowLeastCount = math.ceil((sum(industryLenList) + len(industryLenList)*paddingLeft)* 1.0/(columnMaxLen+paddingLeft))
    print '排序后列表：'
    print industryLenList
    print '列表之和：', sum(industryLenList), '; 行长度限制：', columnMaxLen, '; 间距：', paddingLeft, '; 预计至少需要', rowLeastCount, '行'

    if max(industryLenList) > columnMaxLen: print "单个长度超过行长度限制"
    result = getArray(industryLenList, columnMaxLen, paddingLeft)
    result.sort(key=lambda x:sum(x)+len(x)*2, reverse=True) # 根据结果的行的长度倒排序
    print '结果如下:'
    print result
    print '123456789012345678901234567890'
    for rowIndex in range(len(result)):
        x = ''
        for colIndex in range(len(result[rowIndex])):
            x = x + "X" * result[rowIndex][colIndex] + "  "
        print x
    return


# 主函数
def main():
    industryLenList = [9, 3, 3, 16, 3, 6, 11, 6, 15, 3, 4, 8, 10, 13, 13, 2, 7, 9, 14, 4]
    doList(industryLenList)
    industryLenList = [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
    doList(industryLenList)
    industryLenList = [16, 16, 16, 16, 16, 16, 13, 13, 13, 13, 13, 13]
    doList(industryLenList)
    industryLenList = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    doList(industryLenList)
    industryLenList = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    doList(industryLenList)
    industryLenList = [2, 18, 4, 8, 12, 23, 13, 1, 2, 4, 6, 7, 8, 9, 10, 2, 2, 18, 4, 8, 12, 23, 13, 1, 2, 4, 6, 7, 8, 9, 10, 2]
    doList(industryLenList)

main()
