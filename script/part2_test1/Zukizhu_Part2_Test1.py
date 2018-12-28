#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
import numpy as np
import datetime
import string
import re


class Part2Test1Solution:

    def __init__(self):
        self.__doc__ = "第二次练习题 第一道题"
        self.__author = "zukizhu"

    @staticmethod
    def calc_character(words):
        """
        返回字符、数字重复个数

        :param string words: 输入的待分析语句
        :return [int num, dict my_dict ]:字符个数及字符的重复个数
        """
        dic = {}
        num = 0

        for word in words:
            if not word.isalnum() and word not in ["-", "_", "/"]:
                continue

            if dic.has_key(word):
                dic[word] = dic[word] + 1
            else:
                dic[word] = 1
                num = num + 1

        return [num, dic]


if __name__ == "__main__":
    myWords = "That was your aattempt at 11123 ！flirting?+_. /"
    begin = datetime.datetime.now()
    li = Part2Test1Solution.calc_character(myWords)
    end = datetime.datetime.now()
    runtime = end - begin

    print li
    print runtime

