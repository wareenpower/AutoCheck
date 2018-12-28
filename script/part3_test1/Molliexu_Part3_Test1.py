#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    Testcase operation
    Author          :    Molliexu
    Create time     :    2018-11-23
    Function List   :

"""
import random


class SolutionPart3Test1:

    def __init__(self):
        self.__doc__ = "Part3_Test1"

    @staticmethod
    def check_result(i_list_range, i_list_num, list_compare):

        list_result_max = []
        list_result_min = []

        while True:
            tmp = random.randint(0, i_list_range)
            if tmp not in list_result_max:
                list_result_max.append(tmp)
                if list_compare[0] <= tmp <= list_compare[1]:
                    list_result_min.append(tmp)
            if len(list_result_max) == i_list_num:
                break
        result_min_num = len(list_result_min)

        return list_result_max, list_result_min, result_min_num
