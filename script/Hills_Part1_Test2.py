#coding=utf-8
__author__ = 'hillszhang'

class Part1:

    #hash
    # @staticmethod
    # def threeSum_hash(nums):
    #     result = []
    #     for i, vi in enumerate(nums):
    #         for j, vj in enumerate(nums[i + 1:]):
    #             if 0 - vi - vj in nums[i + 2:]:
    #                 result.append(tuple(sorted([vi, vj, 0 - vi - vj])))
    #     return sorted(list(set(result)))

    #combinations
    @staticmethod
    def Test2(nums):
        from itertools import combinations
        result = []
        for subList in combinations(nums, 3):
            if not sum(subList):
                result.append(tuple(sorted(subList)))
        return sorted(list(set(result)))


    # @staticmethod
    # def threeSum(nums):
    #     result = []
    #     for i in range(0, len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             for x in range(i + 3, len(nums)):
    #                 if nums[i] + nums[j] + nums[x] == 0:
    #                     result.append([nums[i], nums[j], nums[x]])
    #     return result
    # #sort
    # @staticmethod
    # def threeSum_sort(nums):
    #     nums.sort()
    #     lenNums = len(nums)
    #     result = []
    #     if lenNums < 3:
    #         return result
    #     for i in range(0, lenNums - 1):
    #         left, right = i + 1, lenNums - 1
    #         while left < right:
    #             s = nums[i] + nums[left] + nums[right]
    #             if s == 0:
    #                 result.append([nums[i], nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1
    #             elif sum < 0:
    #                 left += 1
    #             else:
    #                 right -= 1
    #     return result
    #


if __name__ == "__main__":
    result = Part1.Test2([-4, -2, -1, 0, 1, 1, 2, 4])
    print result

