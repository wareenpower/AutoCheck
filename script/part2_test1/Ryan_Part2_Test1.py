#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Class2Solution:
    def __init__(self):
        self.__doc__ = "Class 2 Test 1"
        self.__author = "Ryanzhan"

    @staticmethod
    def solution(mstr):
        """
        count character
        :param mstr:string
        :return: [ num, {'character':count, ... }]
        """
        result_dic = {}
        for mchar in mstr:
            if not mchar.isalnum():
                continue
            if mchar in result_dic:
                result_dic[mchar] = result_dic[mchar] + 1
                continue
            result_dic[mchar] = 1

        return len(result_dic), result_dic
