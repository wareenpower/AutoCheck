# -*- coding:utf-8 -*-
import re


class Solution:

    def __init__(self):
        self.__doc__ = "this is test object for ruby"
        self.__author = "ruby"

    @staticmethod
    def calculate_num(string):
        char_num = 0
        global dict_string
        dict_string = {}
        for str_tmp in string:
            if re.match('[0-9A-Za-z_]', str_tmp):
                if str_tmp in dict_string:
                    dict_string[str_tmp] += 1
                else:
                    dict_string[str_tmp] = 1
                    char_num = char_num + 1
        # print char_num, dict_string
        return char_num, dict_string
