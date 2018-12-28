#! /usr/bin/env python
# -*- coding:utf-8 -*-

import random


class RanSolution:
    def __init__(self):
        self.__doc__ = "This is my solution fot the skill test2"
        self.__author__ = "Hua"

    @staticmethod
    def is_ran(int_range, l_number, com_scope):
        """
        Given one random range , list number  and the compare scope, return the random list and sublist and the len of
        child list in the compare scope

        :param int int_range: the range of random
        :param init l_number: the len of random list
        :param list com_scope: the range of sublist
        :return: list list_random: the random list
        :return: list list_scope:  the child  list in the compare scope
        :return: int child_len :the len of sublist in the compare scope
        """
        re_list = []
        start = com_scope[0]
        end = com_scope[1]
        target = []
        list_range = random.sample(range(0, int_range), l_number)
        re_list.append(list_range)

        for m in range(len(list_range)):
            if start <= list_range[m] <= end:
                target.append(list_range[m])
        len_target = len(target)

        return list_range, target, len_target



