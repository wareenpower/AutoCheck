# -*- coding:utf-8 -*-
import string


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def test(x):
        alphas = string.ascii_letters + '_'
        nums = string.digits
        mark = {}
        for c in x:
            if c in alphas + nums:
                mark[c] = mark.get(c, 0) + 1

        return len(mark), mark


if __name__ == "__main__":
    str_test = 'We are fasdasdfasdfadf2q341234adf,./,/ipmissy1122—_.'
    obj1 = Solution()
    print obj1.test(str_test)
