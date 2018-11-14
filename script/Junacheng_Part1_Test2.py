#!/usr/bin/env python
# -*- coding:utf-8 -*-
import doctest


class EqualZeroSeqTest:
    def __init__(self):
        self.__doc__ = "Part1_Test2"
        self.__desc__ = "This is the answer for EqualZeroSeqTest in 2018-10-25 !"
        self.__author = "Junacheng"

    @staticmethod
    def compute_equal_zero_seq(list_integer_input):
        """
        Given a list of integers list_integer_input,return the result list composed of sublist of 3 integers which sums equal to zero

        :param list list_integer_input: a list of integers
        :return:a list of tuple of 3 integers which sums equal to zero

        Example
        -------
        >>> #1. one case that has more than one result lists
        >>> EqualZeroSeqTest().compute_equal_zero_seq([-1, -4, -1, 0, 1, 2, 3, 4])
        [(-4, 0, 4), (-4, 1, 3), (-1, -1, 2), (-1, 0, 1)]
        >>> #2. one case that has no result lists
        >>> EqualZeroSeqTest().compute_equal_zero_seq([-2,-9,0,12,10,3,4])
        []
        """

        list_equal_zero_seq = []

        if not isinstance(list_integer_input, list) or len(list_integer_input) < 3:
            return list_equal_zero_seq

        sorted_list_input = sorted(list_integer_input)
        len_sorted_list_input = len(sorted_list_input)

        beg = 0
        end = len_sorted_list_input - 1
        mid = beg + 1

        while sorted_list_input[beg] <= 0:
            if beg > 0 and sorted_list_input[beg] == sorted_list_input[beg - 1]:
                beg = beg + 1
                continue
            mid = beg + 1
            end = len_sorted_list_input - 1
            while mid < end:
                int_beg = sorted_list_input[beg]
                int_mid = sorted_list_input[mid]
                int_end = sorted_list_input[end]
                int_sum = int_beg + int_mid + int_end
                if int_sum > 0:
                    end = end - 1
                    continue
                if int_sum == 0:
                    list_equal_zero_seq.append((int_beg, int_mid, int_end))
                    while mid < end and sorted_list_input[mid] == sorted_list_input[mid + 1]:
                        mid = mid + 1
                    mid = mid + 1
                    end = end - 1
                    continue
                if int_sum < 0:
                    mid = mid + 1
                    continue

            beg = beg + 1

        return list_equal_zero_seq


if __name__ == "__main__":

    print EqualZeroSeqTest().compute_equal_zero_seq([-1, -4, 0, 1, 2, 3, 4])
