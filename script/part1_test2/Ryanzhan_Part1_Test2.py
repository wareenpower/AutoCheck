#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Solution(object):

    def __init__(self):
        self.__doc__ = "This is test2 by ryanzhan"
        self.__author = "Ryanzhan"

    @staticmethod
    def three_sum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        lennums = len(nums)

        for i in range(lennums):
            left = i + 1
            right = lennums - 1

            if i > 0 and nums[i - 1] == nums[i]:
                left += 1
                continue

            while left < right:
                sumthree = nums[i] + nums[left] + nums[right]
                if sumthree == 0:
                    res.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1

                if sumthree < 0:
                    left += 1
                if sumthree > 0:
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    result_list = s.three_sum([-1, 0, 1, 2, -1, -4])
