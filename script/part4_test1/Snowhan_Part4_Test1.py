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

    @staticmethod
    def get_prefix(list_input):
        s1 = min(list_input)
        s2 = max(list_input)
        print s1, s2
        for i, j in enumerate(s1):
            if j != s2[i]:
                return s1[:i]
        return s1
