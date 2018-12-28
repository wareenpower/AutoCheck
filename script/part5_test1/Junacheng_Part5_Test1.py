#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MapSkillTest:
    def __init__(self):
        self.__doc__ = "This is the answer for MapSkillTest in 2018-11-15 !"
        self.__author = "Junacheng"

    @staticmethod
    def map_skill_test(str_json, key_list, value_list):
        """
        map_skill_test
        :param str str_json: str_json
        :param list key_list: key_list
        :param list value_list: value_list
        :return dict:
        """
        dict_json = eval(str_json)

        if len(key_list) != len(value_list):
            return dict_json

        for index in range(len(key_list)):
            key_item = key_list[index]
            key_item = key_item.strip('/')
            # split key_item into list
            list_key_item = key_item.split('/')
            # get the whole map
            tmp_value = dict_json
            # reset the last item to be set new value
            local_sub_index = -1
            # for-loop to get the last but one item
            for sub_index in range(len(list_key_item) - 1):
                local_sub_index = sub_index
                sub_key_item = list_key_item[sub_index]

                if isinstance(tmp_value, list):
                    tmp_value = tmp_value[int(sub_key_item)]
                else:
                    tmp_value = tmp_value[sub_key_item]
            # get the key of the item to be set new value
            sub_key_item = list_key_item[local_sub_index + 1]
            # set new value
            tmp_value[sub_key_item] = value_list[index]

        return dict_json
