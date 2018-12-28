#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    get_list
    Author          :    Snow  han
    Create time     :    2018-11-5
    Function List   :

"""
import re


class t_check:
    """
        This class has only one function
    """

    def __init__(self):
        pass

    @staticmethod
    def get_list_2(str_input1):
        """

        :param str_input1:
        :return:
        """

        list_res, dict_res = [], {}
        list_res = re.findall("\w", str_input1)
        for i in list_res:
            if i in dict_res:
                dict_res[i] = dict_res[i] + 1
                continue
            dict_res[i] = 1
        return len(dict_res), dict_res


# print t_check.check_data("12398", "879231")
# print t_check.get_list([-10, 2, 3, 4, 5, 6, 7, -2, -5, -7, -1, 100, 12])
print t_check.get_list_2("wo0002222__ are you")
