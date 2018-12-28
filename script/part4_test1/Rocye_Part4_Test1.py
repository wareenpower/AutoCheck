#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def __init__(self):
        self.__author = "Rocye"

    @staticmethod
    def find_max_substring(src_list):
        """
        找出最长公共子串

        :param src_list: [‘apple’, ‘append’, ‘app’]
        :return: ‘app'  (如果没有子串，返回“”)  
        """

        # 空列表直接返回""
        if len(src_list) == 0:
            return ""

        # 获取列表中最小的字符串
        min_len = len(src_list[0])
        min_str = src_list[0]
        for para in src_list:
            if min_len > len(para):
                min_len = len(para)
                min_str = para

        # 生成最小长度字符串的子串列表，按字符数排序
        min_list_has_repeat = [min_str[i:i+x+1] for x in range(len(min_str)) for i in range(len(min_str) - x)]

        # 去重
        min_list = []
        for tmp in min_list_has_repeat:
            if tmp not in min_list:
                min_list.append(tmp)
        mlist = min_list[-1::-1]

        # 获取最大的子串
        for sub_str in mlist:
            cou_index = 0
            for tmp_str in src_list:
                if sub_str not in tmp_str:
                    break
                cou_index = cou_index + 1
            if cou_index == len(src_list):
                return sub_str
        return ""
