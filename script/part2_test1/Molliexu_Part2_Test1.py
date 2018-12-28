#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    Testcase operation
    Author          :    Molliexu
    Create time     :    2018-11-09
    Function List   :

"""
import re

class SolutionPart2Test1:

    def __init__(self):
        self.__doc__ = "Part2_Test1"

    @staticmethod
    def check_result(str_para):
        """
        :param str_para:string
        :return: list_result
        """
        list_result = []
        dict_string_num = {}
        i_num = 0

        for str in str_para:
            if not re.match('[a-zA-Z0-9_]',str):
                continue
            if str in dict_string_num:
                dict_string_num[str] += 1
            else :
                dict_string_num[str] = 1
                i_num +=  1

        return i_num, dict_string_num
