#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random


class CLass3Solution:
    def __init__(self):
        self.__doc__ = "Class 3  test 1"
        self.__author = "Ryanzhan"

    @staticmethod
    def rand_result(int_range, list_number, compare_scope):
        """
        count character
        :param int_range:max number
        :param list_number:random number count
        :param compare_scope:compare scope
        :return: [ num, {'character':count, ... }]
        """
        result_list = []
        count = 0
        if compare_scope[0] <= compare_scope[1]:
            start = compare_scope[0]
            end = compare_scope[1]
        else:
            start = compare_scope[1]
            end = compare_scope[0]
        random_list = random.sample(range(0, int_range), list_number)
        for i in range(list_number):
            if start <= random_list[i] <= end:
                result_list.append(random_list[i])
                count = count + 1
        return random_list, result_list, count