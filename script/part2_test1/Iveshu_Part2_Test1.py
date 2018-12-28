#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re


class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is answer for skill test1 of part2"
        self.__author = "Iveshu"

    @staticmethod
    def get_dict(str_para):
        """
        Get the number of non-repeating characters of a string and the number of times each character appears

        :param str str_para: The input parameter
        :return: Number of non-repeated characters and a dictionary of the number of characters
        """
        dict_result = {}
        list_result = re.findall("\w", str_para)
        for item in list_result:
            dict_result[item] = dict_result.get(item, 0) + 1
        return len(dict_result.keys()), dict_result


if __name__ == "__main__":
    import datetime
    start = datetime.datetime.now()
    print TestSkillSolution.get_dict("We are fasdasdfasdfadf2q341234adf,./,/ipmissy1122—_.")
    end = datetime.datetime.now()
    print (end - start).total_seconds()
