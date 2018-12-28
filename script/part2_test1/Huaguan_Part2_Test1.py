#! /usr/bin/env python
# -*- coding:utf-8 -*-
import re


class StrCount:
    def __init__(self):
        self.__doc__ = "This is my solution fot the skill test2"
        self.__author = "hua"

    @staticmethod
    def character_count(source_str):
        """
        Given one string  return the list of that character and theirs count

        :param string source_str: Source str
        :return: int char_num: char number
        """

        source_str = re.sub("[\s+\.\/,$%^*(\"\']+|[+—!?\[\]~@#￥%&*()]", '', source_str)
        result_list = {}
        for i in source_str:
            result_list[i] = source_str.count(i)

        char_num = len(result_list)
        return char_num, result_list
