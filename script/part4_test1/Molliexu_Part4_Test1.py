#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    Testcase operation
    Author          :    Molliexu
    Create time     :    2018-12-20
    Function List   :

"""


class SolutionPart4Test1:

    def __init__(self):
        self.__doc__ = "Part4_Test1"

    @staticmethod
    def check_result(list_para):
        result = ""
        if len(list_para) == 0:
            return result
        for each in zip(*list_para):
            if len(set(each)) == 1:
                result += each[0]
            else:
                return result
        return result
