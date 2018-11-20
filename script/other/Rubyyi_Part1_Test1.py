# -*- coding:utf-8 -*-
import operator


class Solution3:

    def __init__(self):
        self.__doc__ = "This is test1 for ruby"
        self.__author = "rubyyi"

    def cmp_anagram(self, str1, str2):
        list1 = list(str1)
        list2 = list(str2)
        list1.sort()
        list2.sort()
        print (list1)
        print (list2)
        return operator.eq(list1, list2)


if __name__ == "__main__":
    s1 = "anagram"
    t1 = "nagaram"
    obj1 = Solution3()
    obj1.cmp_anagram(s1, t1)
    s2 = "cat"
    t2 = "bct"
    obj2 = Solution3()
    obj2.cmp_anagram(s2, t2)
