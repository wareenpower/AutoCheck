# -*- coding:utf-8 -*-
import random


class Solution:

    def __init__(self):
        self.__doc__ = "this is test num for ruby"
        self.__author = "ruby"

    @staticmethod
    def random_list(int_range, list_number, list_scope):
        """
        在指定范围内，生成指定元素个数的，非重的随机列表，输出随机list中，并输出用户给定区间的子列表和子列表的长度
        :param int_range: 生成列表的区间
        :param list_number:生成随机列表的个数
        :param list_scope:生成列表的范围
        :return:随机生成的含有list_number个数的列表，列表元素在list_scope区间的元素组成的列表，区间元素个数
        """
        # list_range = []
        list_min = []
        list_tmp = range(0, int_range)
        list_range = random.sample(list_tmp, list_number)
        for tmp_int in list_range:
            if (tmp_int <= list_scope[1]) and (tmp_int >= list_scope[0]):
                    list_min.append(tmp_int)
        return list_range, list_min, len(list_min)


if __name__ == "__main__":
    Solution.random_list(1000, 100, [100, 800])
    # print list_num
    # print list_num2
    # print list_num2_len
