#!/usr/bin/env python
# -*- coding:utf-8 -*-
# import doctest
import random


class NumberTest:

    def __init__(self):
        self.__doc__ = "This is the answer for NumberTest in 2018-11-01 !"
        self.__author = "Junacheng"

    @staticmethod
    def compute_random(int_range, int_list_number, list_compare_scope):
        """

        Given the range of numbers,the number of random integers list,\
        generate specified random numbers in the range of int_range ,and \
        calculate the number of random integer which lies in list_compare_scope,\
        return a list of specified random numbers , a list of random integer and its length

        :param int int_range:the range of numbers
        :param int int_list_number:the number of random integers list
        :param list list_compare_scope:the list of compare scope
        :return:a list of specified random numbers , a list of random integer and its length


        Example
        #answer is not specified!
        -------
        #>>> NumberTest().compute_random(100,10,[20,70])
        #perhaps  ([47, 70, 55, 33, 0, 4, 1, 9, 96, 8], [47, 70, 55, 33], 4) is a right answer
        """

        if not (isinstance(int_range, int) and int_range >= 0):
            return
        if not (isinstance(int_list_number, int) and int_list_number >= 0):
            return
        if not (isinstance(list_compare_scope, list) and len(list_compare_scope) == 2 and list_compare_scope[1] >= list_compare_scope[0]):
            return

        # list_range_scope_res = []
        # list_range_res = []
        int_range_begin = list_compare_scope[0]
        int_range_end = list_compare_scope[1]

        # method 1
        # i = 1
        # while i <= int_list_number:
        #     int_tmp_random = random.randint(0, int_range)
        #     if int_range_begin <= int_tmp_random <= int_range_end:
        #         list_range_scope_res.append(int_tmp_random)
        #     list_range_res.append(int_tmp_random)
        #     i += 1

        # method 2
        list_range = range(int_range)
        list_range_res = random.sample([i for i in list_range], int_list_number)
        list_range_scope_res = [i for i in list_range_res if int_range_begin <= i <= int_range_end]
        return list_range_res, list_range_scope_res, len(list_range_scope_res)


print NumberTest().compute_random(100, 10, [20, 70])

# doctest.testmod(verbose=True)
