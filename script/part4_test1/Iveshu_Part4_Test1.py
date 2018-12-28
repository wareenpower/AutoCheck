#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Part4Test1Solution:

    def __init__(self):
        self.__doc__ = "This class is used to update the values of the dictionary's keys"

    @staticmethod
    def get_same_prefix(list_str):
        
        list_result = map(set, zip(*map(list, list_str)))
        str_result = ''
        for value in list_result:
            if len(list(value)) > 1:
                break
            str_result = str_result + str(list(value)[0])
        return str_result


if __name__ == "__main__":
    # ''.join(map(lambda x: list(x)[0] if len(x) == 1 else '', map(set, zip(*map(list, list_str)))))
    list_test = ["Apple", "AppStore", "Appsss"]
    list_test1 = ["Apple", "APPStore", "Appsss"]
    list_test2 = ["1Apple", "1AppStore", "1Appsss"]
    list_test3 = ["1Apple", "1AppStore", "12Appsss"]

    print(Part4Test1Solution.get_same_prefix(list_test))
    print(Part4Test1Solution.get_same_prefix(list_test1))
    print(Part4Test1Solution.get_same_prefix(list_test2))
    print(Part4Test1Solution.get_same_prefix(list_test3))
