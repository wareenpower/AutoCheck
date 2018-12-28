#coding:utf-8
__author__ = 'hillszhang'
import random


class Part2():
    def __init__(self):
        self.__doc__ = "part2.test1"

    @staticmethod
    def Test1(right, length, scope):
        """
        在指定范围内，生成一个固定元素个数的，不重复的随机列表，输出随机list中，在用户给定区间的子列表，和子列表的长度

        :param int right: 随机数的范围
        :param int length: 随机数的个数
        :param list scope: 随机数的范围检查
        :return: Number of non-repeated characters and a dictionary of the number of characters
        """

        sourceList = random.sample(range(right), length)
        extendList = sourceList + scope
        extendList.sort()
        start = extendList.index(min(scope)) + 1
        end = length + 1 - extendList[::-1].index(max(scope))
        return sourceList, extendList[start:end], end-start

if __name__ == "__main__":
    print Part2.Test1(100, 10, [2, 60])
