#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Class1Solution:
    def __init__(self):
        self.__doc__ = "This is solution for class 1"
        self.__author = "rocye"

    @staticmethod
    def get_3_sum_0_element(list_num):
        """
        get_3_sum_0_element

        :param list_num: source list, num
        :return: all sum 0 lists
        """
        result_list = []

        # sort list
        list_num.sort()

        list_len = len(list_num)
        # get sum=0 element
        for i in range(list_len - 2):
            if i > 0 and list_num[i] == list_num[i-1]:
                continue
            tmp = i
            left_biaoji = i + 1
            right_biaoji = list_len - 1
            while left_biaoji < right_biaoji:
                tmpsum = list_num[tmp] + list_num[right_biaoji] + list_num[left_biaoji]
                if tmpsum > 0:
                    right_biaoji = right_biaoji - 1

                elif tmpsum < 0:
                    left_biaoji = left_biaoji + 1

                else:
                    result_list.append((list_num[tmp], list_num[left_biaoji], list_num[right_biaoji]))
                    while left_biaoji < right_biaoji and list_num[left_biaoji] == list_num[left_biaoji+1]:
                        left_biaoji += 1
                    while left_biaoji < right_biaoji and list_num[right_biaoji] == list_num[right_biaoji-1]:
                        right_biaoji -= 1
                    left_biaoji = left_biaoji + 1
                    right_biaoji = right_biaoji - 1
        return result_list
