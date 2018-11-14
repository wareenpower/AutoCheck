#!/usr/bin/env python
# -*- coding:utf-8 -*-


class TestSolution:

    def __init__(self):
        self.__doc__ = "Part1_Test2"

    @staticmethod
    def three_sum(nums):
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l_t, r = i+1, len(nums)-1
            while l_t < r:
                s = nums[i] + nums[l_t] + nums[r]
                if s < 0:
                    l_t += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l_t], nums[r]))
                    while l_t < r and nums[l_t] == nums[l_t+1]:
                        l_t += 1
                    while l_t < r and nums[r] == nums[r-1]:
                        r -= 1
                    l_t += 1
                    r -= 1
        return res


if __name__ == "__main__":

    list_test = [-10, 2, 3, 4, 5, 6, 7, -2, -5, -7, -1, 100, 12]

    print TestSolution.three_sum(list_test)
