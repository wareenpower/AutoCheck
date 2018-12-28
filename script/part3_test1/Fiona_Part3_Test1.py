#!/usr/bin/env python
# -*- coding:utf-8 *

import random

class IntRange:
    def __init__(self):
        self.__doc__ = 'training Part3_Test1'
        self.__author = 'Fionazhan'

    @staticmethod
    def rangeit(a,b, alist):
        rand1 = random.sample(xrange(a), b)
        sublist = [x for x in rand1 if x >= alist[0] and x <= alist[1]]
        return rand1,sublist,len(sublist)

a = IntRange

print a.rangeit(100, 10, [20, 70])
