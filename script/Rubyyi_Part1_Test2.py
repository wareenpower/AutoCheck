# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.__doc__ = "This is test1 for ruby"
        self.__author = "rubyyi"

    @staticmethod
    def add_data(array):
        """

        :type array: array
        """
        res = []
        res1 = []
        array.sort()
        #print array

        len_array = len(array)

        for i in range(0, len_array - 2):
            j = i + 1
            k = len_array - 1
            while k > j:
                if array[i] + array[j] + array[k] == 0:
                    #print array[i], array[j], array[k]
                    res.append((array[i], array[j], array[k]))
                    j = j + 1
                    k = k - 1
                elif array[i] + array[j] + array[k] > 0:
                    k = k - 1
                else:
                    j = j + 1
        #print res
        for item in res:
            if item not in res1:
                res1.append(item)
        #print res1
        return res1


if __name__ == "__main__":
    test_array1 = [-1, 0, 1, 2, 3, 4]
    test_array2 = [-2, -5, 0, 1, 2, 3, 4]
    test_array3 = [8, 8, 2, -5, -4, -3, -3, -2, 0, 1, 3, 4]
    obj1 = Solution()
    #obj1.add_data(test_array1)
    obj2 = Solution()
    #obj2.add_data(test_array2)
    obj3 = Solution()
    obj3.add_data(test_array3)