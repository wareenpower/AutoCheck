#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections


class Solution(object):

    def __init__(self):
        self.__doc__ = "This is test2 by ryanzhan"
        self.__author = "Ryanzhan"

    @staticmethod
    def three_sum(nums):
        res_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    res_trp=(nums[i], nums[j], nums[k])
                    res_list.append(res_trp)
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list


if __name__ == '__main__':
    s = Solution()
    result_list = s.three_sum([-1, 0, 1, 2, -1, -4])
    print result_list