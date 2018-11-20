#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import datetime
import numpy as np


class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is answer for skill test1 of part3: Number"

    @staticmethod
    def get_number(int_range, int_number, list_scope):
        """
        在指定范围内，生成一个固定元素个数的，不重复的随机列表，输出随机list中，在用户给定区间的子列表，和子列表的长度

        :param int int_range: 随机数的范围
        :param int int_number: 随机数的个数
        :param list list_scope: 随机数的范围检查
        :return: Number of non-repeated characters and a dictionary of the number of characters
        """

        list_source, list_cmp = [], []

        i_count = 0
        int_min, int_max = list_scope[0], list_scope[1]

        # list_source = np.random.randint(0, int_range, int_number)

        # for i_item in list_source:
        #     if int_min <= i_item <= int_max:
        #         list_cmp.append(i_item)

        while i_count < int_number:

            i_item = random.randint(0, int_range)
            if i_item not in list_source:
                list_source.append(i_item)
                i_count += 1

                if int_min <= i_item <= int_max:
                    list_cmp.append(i_item)

        return sorted(list_source), sorted(list_cmp), len(list_cmp)


if __name__ == "__main__":

    start = datetime.datetime.now()
    i_range = 100
    i_number = 10
    list_scope_1 = [20, 70]

    print TestSkillSolution.get_number(i_range, i_number, list_scope_1)
    end = datetime.datetime.now()
    print (end - start).total_seconds()
