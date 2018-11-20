#! /usr/bin/env python
# -*- coding:utf-8 -*-


class SumSolution:
    def __init__(self):
        self.__doc__ = "This is my solution fot the skill test2"
        self.__author__ = "Hua"

    @staticmethod
    def is_sum(source_list):
        """
        Given one array source_arr and one int target, return the list of that sum is the target

        :param list source_list: Source array
        :return: the list
        """
        source_list.sort()
        result = []
        end = len(source_list)
        target = 0
        for m in range(end - 1):
            if source_list[0] > target:
                result = []

            for n in range(m+1, end-1):
                temp = source_list[m] + source_list[n]
                if (target - temp) in source_list[n+1::]:
                    tt = (source_list[m], source_list[n], target - temp)
                    if tt not in result:
                        result.append(tt)
        return result


#if __name__ == '__main__':
#    csobject = SumSolution()
#    target = 0
#    a1= [0, 0, 0, 0, -1, 1, -2, 1]
#    a2 = [1, 1, 2, 2, -1, -1, -3, -4, -6, -7, -100, 90, 10000, 30000, -20000, -10000]
#    a3 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, -1, -1, -1, -1, -1, -1, 0, -2]

#    r1 = csobject.is_sum(a1)
#    r2 = csobject.is_sum(a2)
#    r3 = csobject.is_sum(a3)

#    print r1, r2, r3, r4
