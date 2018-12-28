#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Function        :    get_list
    Author          :    Snow  han
    Create time     :    2018-11-5
    Function List   :

"""

import json


class t_check:
    """
        This class has only one function
    """

    def __init__(self):
        pass

    @staticmethod
    def get_dict(json_input, list_key, list_value):
        """

        :param json_input:
        :param list_key:
        :param list_value:
        :return:
        """
        dict_json = json.loads(json_input)
        j = 0
        for i, str_key in enumerate(list_key):
            sub_key = str_key.split("/")
            del sub_key[0]
            dict_tmp = dict_json
            for key, value in enumerate(sub_key):
                if key + 1 == len(sub_key):
                    break
                if isinstance(dict_tmp, dict):
                    dict_tmp = dict_tmp[value]
                    continue
                if isinstance(dict_tmp, list):
                    int_index = int(value)
                    dict_tmp = dict_tmp[int_index]
            dict_tmp[sub_key[-1]] = list_value[j]
            j = j + 1
        return dict_json
