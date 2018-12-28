# encoding:utf-8
import random


# 题目一：
# 1、在一个范围内,生成一个固定元素个数的,不重复的随机list.
#   先用 range(1,all_num) 得到  1-100 的列表


class TestNumber:

    def __init__(self):
        self.__doc__ = "This is number test"
        self.__author = "Baby"

    @staticmethod
    def list_son(int_range, int_length, list_scope):
        """
       在指定范围内，生成指定元素个数的，非重的随机列表，输出随机list中，并输出用户给定区间的子列表和子列表的长度

       :param int int_range: 随机数的范围
       :param int int_length: 随机数的个数
       :param list list_scope: 随机数的范围检查
       :return: Number of non-repeated characters and a dictionary of the number of characters
       """

        list_min = list_scope[0]
        list_max = list_scope[1]
        list_random = random.sample(range(0, int_range), int_length)
        list_son = []
        # 2 计算随机list中，在用户给定区间内子列表
        for i in range(0, len(list_random)):
            if list_min <= list_random[i] <= list_max:
                list_son.append(list_random[i])

        return list_random, list_son, len(list_son)


if __name__ == "__main__":
    print TestNumber.list_son(100, 5, [10, 20])
