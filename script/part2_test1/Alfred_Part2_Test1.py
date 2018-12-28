#!/usr/bin/env python
# -*- coding:utf-8 *

import string

class Solutions:
    def __init__(self):
        self.__doc__ = 'training Part2_Test1'
        self.__author = 'Alfredwu'

    @staticmethod
    def count_dict(str_para):
        """


        :param str:  输入字符串
        :return:  打印[字符个数，{每个字符出现的次数}]
        """

        list_str = [x for x in str_para if x in string.letters or x in string.digits]

        return [len(list_str), {key: list_str.count(key) for key in set(list_str)}]
