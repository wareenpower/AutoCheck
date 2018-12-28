#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    get_list
    Author          :    Snow  han
    Create time     :    2018-11-5
    Function List   :

"""

import random


class t_check:
    """
        This class has only one function
    """

    def __init__(self):
        pass

    @staticmethod
    def get_list_3(int_range, int_num, comp_scope):
        """

        :param int_range:
        :param int_num:
        :param comp_scope:
        :return:
        """

        list_data, sub_list_data = [], []
        list_data = random.sample(xrange(0, int_range + 1), int_num)
        for i in list_data:
            if comp_scope[0] <= i <= comp_scope[1]:
                sub_list_data.append(i)
        return list_data, sub_list_data, len(sub_list_data)


# print t_check.check_data("12398", "879231")
# print t_check.get_list([-10, 2, 3, 4, 5, 6, 7, -2, -5, -7, -1, 100, 12])
print t_check.get_list_3(100, 10, [20, 70])
