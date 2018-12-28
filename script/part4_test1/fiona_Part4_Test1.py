#!/usr/bin/env python
# -*- coding:utf-8 -*-

def match_me(minest, astring):
    if minest == "":
        return ""
    if astring.startswith(minest):
        return minest
    else:
        minest = minest[:-1]
        return match_me(minest, astring)


class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is example for skill test"
        self.__author = "fiona2"


    @staticmethod
    def list_match(alist):
        minest = min(alist, key=len)
        for item in alist:
            minest = match_me(minest,item)
        return minest
