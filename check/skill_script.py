# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        self.__doc__ = "this is test dict for ruby"
        self.__author = "ruby"

    @staticmethod
    def dict_subject(input_json, key_list, value_list):
        """
        将字符串中某些key的值修改为给定的value，并将修改后的json字符串以字典形式输出
        :param value_list: 需要修改的值
        :param key_list: key的列表
        :param input_json: 输入的字符串字典
        :return:返回修改后的字符串
        """
        try:
            import json
            dict_input = json.loads(input_json)
            i = 0
            for key in key_list:
                key_split = key.split('/')
                key_split.pop(0)
                dict_out = Solution()._get_last_value(dict_input, key_split)
                dict_out[key_split[-1]] = value_list[i]
                i = i + 1
        except Exception as e:
            print e.message
            pass
        return dict(dict_input)

    @staticmethod
    def _get_last_value(input_json, key_split):
        """
        根据key_split获取输入字典的待修改的值
        :param key_split: 分割符
        :param input_json: 输入的字符串字典
        :return:返回修改后的字符串
        """
        try:
            output_json = input_json
            for key, value in enumerate(key_split):
                if key == len(key_split) - 1:
                    break
                if isinstance(output_json, dict):
                    output_json = output_json.get(value)
                    continue
                if isinstance(output_json, list):
                    i_index = int(value)
                    output_json = output_json[i_index]
        except Exception as e:
            print e.message
            pass
        return output_json


if __name__ == "__main__":
    dict_info = '''{
        "name": "info",
        "list_1": [
            {"name": "1"},
            {"name": "2"}
        ]
    }'''
    input_json_src = '''{"Id": "101",
                  "header":
                      {"funcNo": "IF01",
                       "mobile": "075512344565"},
                  "payload":
                      {"contact": {"mobile": "123456789999", "wechat": "test"}
                       }
                  }'''
    key_list_src = ['/header/mobile', '/payload/contact/mobile', '/Id']
    value_list_src = ['0755839699', '98443857', '101']
    Solution.dict_subject(input_json_src, key_list_src, value_list_src)
