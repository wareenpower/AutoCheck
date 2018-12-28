#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SequenceTest:

    def __init__(self):
        self.__doc__ = "This is the answer for SequenceTest in 2018-11-15 !"
        self.__author = "Junacheng"

    @staticmethod
    def compute_longest_comm_prefix(str_list):
        """
        compute the longest common prefix of a string list

        :param list str_list: a str list
        :return str: if the longest common prefix is founded ,it will be returned ,otherwise None will be returned.
        """

        # Todo:parameter check

        min_len = len(str_list[0])
        min_item = ''
        for i, str_item in enumerate(str_list):
            if len(str_item) <= min_len:
                min_len = len(str_item)
                min_item = str_item

        index = 0
        tmp_set = set()
        while index < min_len:
            for i, str_item in enumerate(str_list):
                tmp_set.add(str_item[index])
            if len(tmp_set) > 1:
                return min_item[0:index]
            else:
                tmp_set = set()
                index = index + 1

        return min_item[0:min_len]
