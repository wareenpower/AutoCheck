#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


class CLass2Solution:
    def __init__(self):
        self.__doc__ = "Class 2  test 2"
        self.__author = "Rocye"

    @staticmethod
    def rand_result(source_range, num_count, range_list):
        req_list = []
        req_list_after_select = []
        after_select_count = 0

        for i in range(num_count):
            tmp = random.randint(0, source_range)
            while tmp in req_list:
                tmp = random.randint(0, source_range)
            req_list.append(tmp)
            if range_list[0] <= tmp <= range_list[1]:
                req_list_after_select.append(tmp)
                after_select_count = after_select_count + 1

        return req_list, req_list_after_select, after_select_count
