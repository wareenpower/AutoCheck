#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Part6Test1Solution:

    def __init__(self):
        self.__doc__ = "part6 test1 answer"

    @staticmethod
    def triple_kill(i_depth):
        list_item, index = [1], 0
        list_result = [list_item]
        while index < i_depth:
            # yield list_item
            list_item = [1] + [list_item[i] + list_item[i + 1] for i in range(len(list_item) - 1)] + [1]
            list_result.append(list_item)
            index += 1
        return list_result
    #
    # @staticmethod
    # def get_list(i_depth):
    #     list_result = []
    #     for x in Part6Test1Solution().triple_kill(i_depth):
    #         list_result.append(x)
    #     return list_result


if __name__ == "__main__":
    print Part6Test1Solution().triple_kill(4)
