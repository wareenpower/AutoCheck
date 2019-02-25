#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
import os
import importlib


class Part9Test1Solution:

    def __init__(self):
        self.__doc__ = "part9 test1 answer"

    @staticmethod
    def _reg_test(str_module_name):
        """
        calc the result

        :param str_module_name: the each module name
        :return: the each result of the module
        """
        # Get function list
        mod1 = importlib.import_module(str_module_name)
        list_function = [method for method in dir(mod1) if callable(getattr(mod1, method))]
        method_function = getattr(mod1, list_function[0], lambda: "nothing")

        # Get parameters
        list_para_name = [method for method in dir(mod1) if not callable(getattr(mod1, method))]
        list_get_value = []
        # list_get_name = []
        for index, value in enumerate(list_para_name):
            int_data = getattr(mod1, value)
            if isinstance(int_data, int):
                # print index, value, int_data
                list_get_value.append(int_data)
                # list_get_name.append(value)
        # print("Para name:  " + str(list_get_name))
        # print("Parameter list: " + str(list_get_value))

        # Gets the number divided by 4."
        list_value_4 = []
        for index, value in enumerate(list_get_value):
            i_div_4 = value % 20
            str_reg = "^(0|4|8|12|16)$"
            match_result = re.search(str_reg, str(i_div_4))
            if match_result:
                list_value_4.append(value)
        # print("Para result list: {result}".format(result=list_value_4))
        return method_function(list_value_4)

    @staticmethod
    def get_result(module_name):
        """
        Get the module result

        :param module_name: the module name
        :return: the dictionary of the result
        """
        dict_result = {}
        # Get the module list
        str_script_path = os.path.dirname(str(os.path.abspath(__file__)))
        for root, dirs, files in os.walk(str_script_path + os.sep + module_name):
            for each in files:
                # Check module name
                if each.lower().endswith(".py") and each.lower() not in ["__init__.py"]:
                    str_name = each[:-3]
                    # print str_name
                    i_each_result = Part9Test1Solution._reg_test(module_name + "." + str_name)
                    dict_result[str_name] = i_each_result
        return dict_result


if __name__ == "__main__":
    t1 = Part9Test1Solution()
    print(t1.get_result("test_module_2"))
    # print("*" * 100)
    # print 22 % 20
    # print 0 % 20
    # print -0 % 20
    # print -4 % 20
    # print -8 % 20
    # print -12 % 20
    # print -16 % 20
