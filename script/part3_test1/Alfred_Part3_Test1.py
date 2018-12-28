#!/usr/bin/env python
# -*- coding:utf-8 *

import random


class Solutions:
    def __init__(self):
        self.__doc__ = 'training Part3_Test1'
        self.__author = 'Alfredwu'

    @staticmethod
    def gen_nlist(int_range, list_number, compare_scope):
        """

        :param int_range: 生成列表的int值范围
        :param list_number: 生成列表的长度
        :param compare_scope: 过滤列表的范围
        :return: （生成列表，过滤后列表，过滤后列表长度）
        """

        nlist = random.sample([x for x in range(int_range)], list_number)
        filter_nlist = [n for n in nlist if n >= compare_scope[0] and n <= compare_scope[1]]
        return nlist, filter_nlist, len(filter_nlist)
