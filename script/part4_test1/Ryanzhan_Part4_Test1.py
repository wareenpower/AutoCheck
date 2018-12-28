#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Part4Test1Solution:

    def __init__(self):
        pass

    @staticmethod
    def longest_common_prefix(strs):

        rstr = ''
        if len(strs) == 0:
            return rstr
        old = strs[0]
        for i in range(len(old)):
            for j in range(len(strs)):
                try:
                    if old[i] == strs[j][i]:
                        pass
                    else:
                        return rstr
                except:
                    return rstr
            else:
                rstr += old[i]
        return rstr
