#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re


class TestObject:

    def __init__(self):
        self.__doc__ = "This is number test"
        self.__author = "Baby"

    @staticmethod
    def str_number(str_input):
        """
        求出字符列表中字符的个数，并给出各字符出现的频数

        :param str_input: 初始的字符串，string 类型
        :return:返回字符列表中，字符的个数及各字符的频数
        """

        ll = re.findall("[A-Za-z0-9_]", str_input)
        str_fre = {}
        new_ll = set(ll)
        for i in new_ll:
            str_fre[i] = ll.count(i)
        return len(new_ll), str_fre

