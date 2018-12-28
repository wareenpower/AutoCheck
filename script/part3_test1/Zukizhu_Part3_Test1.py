#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
import numpy as np
import datetime
import random


class Part3Test1Solution:

    def __init__(self):
        self.__doc__ = "第三次练习题 第一道题"
        self.__author = "zukizhu"

    @staticmethod
    def random_list(int_range, list_number, compare_score):
        """
        按指定范围返回子集合

        :param int int_range:   如100
        :param int list_number: 如 10
        :param list compare_score: compare scope  如20 70
        :return:
        """
        src_list = []
        des_list = []
        if isinstance(int_range, int) and isinstance(list_number, int) and isinstance(compare_score, list) and len(compare_score) == 2:
            tmp_list = range(int_range)
            src_list = random.sample(tmp_list, list_number)

            for li in src_list:
                if compare_score[0] <= li <= compare_score[1]:
                    des_list.append(li)

        return list(src_list), des_list, len(des_list)


if __name__ == "__main__":
    i_range = 100
    l_number = 10
    c_score = [20, 70]
    begin = datetime.datetime.now()
    date = Part3Test1Solution.random_list(i_range, l_number, c_score)
    end = datetime.datetime.now()
    runtime = end - begin
    print date
    print runtime
