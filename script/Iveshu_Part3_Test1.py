#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random


class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is answer for skill test1 of part3: Number"

    @staticmethod
    def get_number(int_range, int_number, list_scope):
        """
        在指定范围内，生成一个固定元素个数的，不重复的随机列表，输出随机list中，在用户给定区间的子列表，和子列表的长度

        :param int int_range: 随机数的范围
        :param int int_number: 随机数的个数
        :param list list_scope: 随机数的范围检查
        :return: Number of non-repeated characters and a dictionary of the number of characters
        """

        list_source, list_cmp = [], []

        b_do = True
        while b_do:
            # Check input parameters legitimacy
            if int_number > int_range:
                print "Input error: int_number(number) greater than int_range(range)".format(
                    number=int_number, range=int_range)
                break

            if len(list_scope) != 2:
                print "Input error: length of list_scope(scope) invalid".format(
                    scope=list_scope)

            i_count = 0
            int_min, int_max = list_scope[0], list_scope[1]

            if int_min > int_max:
                print "Input error: list_scope(scope) invalid, min greater than max".format(
                    scope=list_scope)
                break
            while i_count < int_number:

                i_item = random.randint(0, int_range)
                if i_item not in list_source:
                    list_source.append(i_item)
                    i_count += 1

                    if int_min <= i_item <= int_max:
                        list_cmp.append(i_item)
            b_do = False

        return sorted(list_source), sorted(list_cmp), len(list_cmp)


if __name__ == "__main__":
    i_range = 100
    i_number = 10
    list_scope_1 = [20, 70]

    print TestSkillSolution.get_number(i_range, i_number, list_scope_1)
    # print TestSkillSolution.get_number(10, 100, [20, 70])
    list_source_1, list_cmp_1, i_len = TestSkillSolution.get_number(100, 10, [20, 70])

    test = [sorted([i for i in list_scope_1 if 10< i < 80]) == list_scope_1]
    print test