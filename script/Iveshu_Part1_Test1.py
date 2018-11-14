#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections


class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is example for skill test"
        self.__author = "Iveshu"

    @staticmethod
    def is_anagram(str_source, str_target):
        """
        Given two strings s and t, return the result whether str_target is a disordered image of str_source

        :param str str_source: Source string
        :param str str_target: Target string
        :return: the bool result
        """
        if len(str_source) != len(str_target):
            return False
        return len(collections.Counter(str_source) - collections.Counter(str_target)) == 0


if __name__ == "__main__":
    print "11"
    print TestSkillSolution.is_anagram("aa", "BB")
