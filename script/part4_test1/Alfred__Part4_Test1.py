#!/usr/bin/env python
# -*- coding:utf-8 *


class Solutions:
    def __init__(self):
        self.__doc__ = 'training work 04'
        self.__author = 'Alfredwu'

    @staticmethod
    def func(nlist):
        """
        列表中所有字符元素最大公共前缀

        :param list nlist: 包含数字的列表
        :return: str
        """

        s1 = min(nlist)
        s2 = max(nlist)
        for i, j in enumerate(s1):
            if j != s2[i]:
                return s1[:i]
        return s1
