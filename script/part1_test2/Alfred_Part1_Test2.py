#!/usr/bin/env python
# -*- coding:utf-8 *


class Solutions:
    def __init__(self):
        self.__doc__ = 'training work 02'
        self.__author = 'Alfredwu'

    @staticmethod
    def three_sum(nlist):
        """
        列表中任意3个数字和为0

        :param list nlist: 包含数字的列表
        :return: list: [[num1,num2,num3], [num11, num22, num33] ...]
        """
        res = []
        size_nlist = len(nlist)
        if size_nlist < 3:
            return res

        nlist.sort()
        for i in range(size_nlist):
            if nlist[i] > 0:
                break
            if i > 0 and nlist[i] == nlist[i - 1]:
                continue
            left = i + 1
            right = size_nlist - 1
            while left < right:
                if nlist[left] + nlist[right] == -nlist[i]:
                    res.append((nlist[i], nlist[left], nlist[right]))
                    while left < right and nlist[left] == nlist[left + 1]:
                        left = left + 1
                    while left < right and nlist[right] == nlist[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif nlist[left] + nlist[right] < -nlist[i]:
                    left = left + 1
                else:
                    right = right - 1
        return res
