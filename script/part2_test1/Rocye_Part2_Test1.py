#! /usr/bin/env python
# -*- coding:utf-8 -*-


class Class2Solution:
    def __init__(self):
        self.__doc__ = "Class 2 Test 1"
        self.__author = "Rocye"

    @staticmethod
    def solution(src_str):
        """
        count character

        :param src_str:
        :return: [ num, {'character':count, ... }]
        """
        src_dic = {}

        for char in src_str:
            if not char.isalnum() and char != '_':
                continue
            if char in src_dic:
                src_dic[char] = src_dic[char] + 1
                continue
            src_dic[char] = 1

        return len(src_dic),src_dic
