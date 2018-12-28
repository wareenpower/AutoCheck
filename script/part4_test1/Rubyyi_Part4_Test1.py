# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        self.__doc__ = "this is part 4 test for ruby"
        self.__author = "ruby"

    @staticmethod
    def comm_str(list_str):
        """
        在字符串的数组中，找出该字符串数组的公共前缀，以字符串形式返回，如果无公共前缀，返回空
        :param list_str: 输入的字符串数组
        :return:返回的公共前缀
        """
        if not list_str:
            return ''
        s1 = min(list_str)
        s2 = max(list_str)
        for i, j in enumerate(s1):
            if j != s2[i]:
                return s1[:i]
        return s1


if __name__ == "__main__":
    list_str_src = ['apple', 'append', 'app']
    list_str1 = ['apple', 'banana', 'orange']
    Solution.comm_str(list_str_src)
    # Solution.comm_str(list_str1)
    # print list_num
    # print list_num2
    # print list_num2_len

