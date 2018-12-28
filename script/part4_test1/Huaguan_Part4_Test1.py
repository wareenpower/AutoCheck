#! /usr/bin/env python
# -*- coding:utf-8 -*-


class ListSolution:
    def __init__(self):
        self.__doc__ = "This is my solution fot the skill test2"
        self.__author__ = "Hua"

    @staticmethod
    def same_search(input_list):
        input_list.sort(key=lambda x: len(x))
        base_str = input_list[0]
        list_len = len(base_str)
        for m in range(list_len):
            for com_str in input_list[1:]:
                if com_str[m] != base_str[m]:
                    return base_str[:m]
        return base_str
