# -*- coding:utf-8 -*-
import random


class Solution:

    def __init__(self):
        pass

    @staticmethod
    def test(end, num, x):
        down = x[0]
        up = x[1]
        tmp = random.sample(range(0, end), num)
        res = []
        for y in tmp:
            if down <= y <= up:
                res.append(y)
        return tmp, res, len(res)


if __name__ == "__main__":
    obj1 = Solution()
    print obj1.test(100, 10, [20, 70])

