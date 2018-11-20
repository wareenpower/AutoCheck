#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json


class Part5Test3Solution:

    def __init__(self):
        self.__doc__ = "This class is used to update the values of the dictionary's keys"

    @staticmethod
    def _fmt_int(obj_value):
        int_result = None
        try:
            int_result = int(obj_value)
            return int_result
        except Exception as e:
            print e.message
            return int_result

    @staticmethod
    def _get_last_dict(dict_src, str_item_key_path):
        dict_last = dict_src
        try:
            list_item_key_path = str_item_key_path.split("/")
            list_item_key_path.pop(0)

            for index, value in enumerate(list_item_key_path):
                if index == len(list_item_key_path) - 1:
                    break
                # 更高效的方式是使用try，如果try失败，则认为是list，但是需要保证输入数据都是合法的，
                if isinstance(dict_last, dict):
                    dict_last = dict_last.get(value)
                    continue
                if isinstance(dict_last, list):
                    int_value = Part5Test3Solution()._fmt_int(value)
                    dict_last = dict_last[int_value]
        except Exception as e:
            print e.message
        return dict_last

    @staticmethod
    def update_dict(str_json, list_key_path, list_key_value):
        dict_result = {}
        try:
            dict_info = json.loads(str_json)
            for index, value in enumerate(list_key_path):
                dict_last = Part5Test3Solution()._get_last_dict(dict_info, value)
                dict_last[value.split("/")[-1]] = list_key_value[index]
            dict_result = dict_info
            pass
        except Exception as e:
            print e.message
            pass

        return dict_result


if __name__ == "__main__":
    str_dict_info = """{
                "name": "skill_test",
                "detail": {
                    "part": 5,
                    "test": {
                        "title": "modify the dictionary key's value",
                        "date": "2018-11-17",
                        "temp": {
                            "p1": 12
                        }
                    }
                },
                "list_1": [
                    {"name": "part1"},
                    {"name": "part2"}
                ],
                "int_key": {
                    "name": "int",
                    "0": 1
                }
            }"""

    dict_update = Part5Test3Solution().update_dict(str_dict_info,
                                           ["/detail/test/title", "/name", "/detail/part", "/list_1/1/name", "/int_key/0"],
                                           ["update value", "skill_update", 3, "modify part1 list", 3])
    dict_cmp = {
                "name": "skill_update",
                "detail": {
                    "part": 3,
                    "test": {
                        "title": "update value",
                        "date": "2018-11-17",
                        "temp": {
                            "p1": 12
                        }
                    }
                },
                "list_1": [
                    {"name": "part1"},
                    {"name": "modify part1 list"}
                ],
                "int_key": {
                    "name": "int",
                    "0": 3
                }
            }
    print [dict_update == dict_cmp]
    sep_info = (",", ":")
    obj_json = json.dumps(dict_cmp, separators=sep_info)
    print obj_json
    print type(obj_json)
    print json.loads(obj_json)["list_1"]
