#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    Testcase operation
    Author          :    Molliexu
    Create time     :    2018-11-09
    Function List   :

"""


class SolutionPart1Test2:

    def __init__(self):
        self.__doc__ = "Part1_Test2"

    @staticmethod
    def check_result(list_para):
        """
        :param list_para: the list of nums
        :return: list
        """
        list_result = []
        list_para.sort()
        i_len = len(list_para)

        for index_1 in range(i_len - 2):
            if list_para[index_1] > 0:
                break
            if index_1 > 0 and list_para[index_1] == list_para[index_1 - 1]:
                continue
            index_2 = index_1 + 1
            index_3 = i_len - 1
            while index_2 < index_3:
                i_1 = list_para[index_1]
                i_2 = list_para[index_2]
                i_3 = list_para[index_3]
                if i_1 + i_2 + i_3 < 0:
                    index_2 += 1
                elif i_1 + i_2 + i_3 > 0:
                    index_3 -= 1
                else:
                    list_result.append((i_1, i_2, i_3))
                    while index_2 < index_3 and list_para[index_2] == i_2:
                        index_2 += 1
                    while index_2 < index_3 and list_para[index_3] == i_3:
                        index_3 -= 1
                    if index_2 >= index_3:
                        break
        return list_result
