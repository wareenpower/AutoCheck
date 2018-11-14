# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        pass

    @staticmethod
    def test2(list_input):
        res = []
        list_input.sort()
        for index in range(len(list_input)):

            j = index + 1 # j =1
            k = len(list_input) - 1 # k = 7
            while j < k:
                if list_input[j] + list_input[k] + list_input[index] > 0:
                    k = k - 1
                elif list_input[j] + list_input[k] + list_input[index] < 0:
                    j = j + 1
                else:
                    # print("{0}+{1}+{2}=0".format(list_input[index], list_input[j], list_input[k]))
                    res.append((list_input[index], list_input[j], list_input[k]))
                    while list_input[j] == list_input[j + 1] and j < k:
                        j = j + 1



                    while list_input[k] == list_input[k - 1] and j < k:
                        k = k - 1

                    j = j + 1
                    k = k - 1
        res = list(set(res))
        return sorted(res)


if __name__ == "__main__":
    test_array1 = [-1, 0, 2]
    test_array2 = [-2, -5, 0, -1, -1, 1, 2, 3, 4, -4, 7, 0, 1]
    obj1 = Solution()
    print obj1.test2([-2, -1, 0, 0, 0, 0, 1, 1])
    # obj2 = Solution()
    # print obj2.test2(test_array2)
