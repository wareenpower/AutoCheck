#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
from itertools import combinations

class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is example for skill test"
        self.__author = "fiona"

    @staticmethod
    def check_equle(alist):
        ans = []
        expanded = [var for var in combinations(alist, 3)]
        #print expanded
        for item in expanded:
            if any(n <= 0 for n in item):
                if (item[0]+item[1]+item[2] == 0):
                    tmp = tuple(sorted(item))
                    if tmp not in ans:
                        ans.append(tmp)
            else:
                pass
        return sorted(ans)

if __name__ == "__main__":
    x = TestSkillSolution()
    print x.check_equle([0, 0, 0, 0, -1, 1, -2, 1])




