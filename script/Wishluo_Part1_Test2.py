# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        pass

    @staticmethod
    def test2(l):
        res = []
        l.sort()
        for index in range(len(l)):

            j = index + 1
            k = len(l) - 1
            while j < k:
                if l[j] + l[k] + l[index] > 0:
                    k = k - 1
                elif l[j] + l[k] + l[index] < 0:
                    j = j + 1
                else:
                    # print("{0}+{1}+{2}=0".format(l[index], l[j], l[k]))
                    res.append((l[index], l[j], l[k]))
                    while l[j] == l[j + 1] and j < k:
                        j = j + 1
                    while l[k] == l[k - 1] and j < k:
                        k = k - 1

                    j = j + 1
                    k = k - 1
        res = list(set(res))
        return sorted(res)


if __name__ == "__main__":
    test_array1 = [-1, 0, 2]
    test_array2 = [-2, -5, 0, -1, -1, 1, 2, 3, 4, -4, 7, 0, 1]
    obj1 = Solution()
    print obj1.test2(test_array1)
    obj2 = Solution()
    print obj2.test2(test_array2)
