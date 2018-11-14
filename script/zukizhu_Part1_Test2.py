#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections


class Part1Test2Solution:

    def __init__(self):
        self.__doc__ = "第一次练习题"
        self.__author = "zukizhu"

    @staticmethod
    def _is_anagram(str_source, str_target):
        """
        Given two strings s and t, return the result whether str_target is a disordered image of str_source

        :param str str_source: Source string
        :param str str_target: Target string
        :return: the bool result
        """
        if len(str_source) != len(str_target):
            return False

        return cmp(sorted(list(str_source.lower())),sorted(list(str_target.lower()))) == 0

    @staticmethod
    def zero_list(src_list):
        """
        给出一个包含整数的数组，计算出数组元素中三个值相加等于0的数据序列

        :param list src_list:原始数组
        :return:list dest_list:返回目标数组，如果没用则为空
        """
        list_len= len(src_list)
        if list_len <3:
            return 0

        #print src_list
        src_list.sort()
        left=0 ; mid=1; right=list_len-1

        count = 0
        dest_list = []

        while (left < right - 1 ):
            while ( right > left + 1 ):
                while (mid < right ):
                     midValue = src_list[left] + src_list[mid] + src_list[right]
                     if midValue == 0:
                         dest_list.append( (src_list[left],src_list[mid],src_list[right]))
                         count = count + 1
                         #print det_list
                     mid = mid + 1
                right = right - 1
                mid = left + 1
            left = left + 1
            mid = left + 1
            right = list_len - 1
        #dest_list = list(set(dest_list))
        new_list = []
        for li in dest_list:
            if li not in new_list:
                new_list.append(li)
        return  new_list

if __name__ == "__main__":
    #print TestSkillSolution1.is_anagram("zuki","zski")
    list = [5,3,7,2,1,0,-1,-8,-5]
    print  Part1Test2Solution.zero_list(list)