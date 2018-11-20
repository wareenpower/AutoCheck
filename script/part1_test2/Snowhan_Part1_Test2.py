#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    get_list
    Author          :    Snow  han
    Create time     :    2018-11-5
    Function List   :

"""


class t_check:
    """
        This class has only one function
    """

    def __init__(self):
        pass

    # @staticmethod
    # def check_data(input1, input2):
    #     """
    #     check_data
    #     :param input1:
    #     :param input2:
    #     :return the result for checking input1 == input2 :
    #     """
    #     list_input1, list_input2 = [], []
    #     for i in input1:
    #         list_input1.append(i)
    #     for j in input2:
    #         list_input2.append(j)
    #     list_input1.sort()
    #     list_input2.sort()
    #     return list_input1 == list_input2

    @staticmethod
    def get_list(list_input1):
        """

        :param list_input1:
        :return: res_list
        """
        res_list = []
        list_input1.sort()
        for i in range(len(list_input1) - 2):
            if i > 0 and list_input1[i] == list_input1[i - 1]:
                continue
            m, n = i + 1, len(list_input1) - 1
            while m < n:
                i_sum = list_input1[i] + list_input1[m] + list_input1[n]
                if i_sum < 0:
                    m += 1
                elif i_sum > 0:
                    n -= 1
                else:
                    sub_list = (list_input1[i], list_input1[m], list_input1[n])
                    while m < n and list_input1[m] == list_input1[m + 1]:
                        m += 1
                    while m < n and list_input1[n] == list_input1[n - 1]:
                        n -= 1
                    m += 1
                    n -= 1
                    res_list.append(sub_list)
        return res_list


# print t_check.check_data("12398", "879231")
print t_check.get_list([-10, -10, -10, 4, 5, -2, 7, 0, -12, -7, 0, 12, 12])
