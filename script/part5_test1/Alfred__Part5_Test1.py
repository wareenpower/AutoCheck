#!/usr/bin/env python
# -*- coding:utf-8 *

import json

class Solutions:
    def __init__(self):
        self.__doc__ = 'training work 05'
        self.__author = 'Alfredwu'

    @staticmethod
    def func(input_json, key_list, value_list):
        ret_dict = json.loads(input_json)

        for key, value in zip(key_list,value_list):
            tmp_dict = ret_dict
            key_path = key.split('/')[1:]
            for i, tmp_key in enumerate(key_path):
                if i == len(key_path) - 1:
                    break
                if tmp_key in ('0','1','2','3','4','5','6','7','8','9'):
                    tmp_key = int(tmp_key)
                tmp_dict = tmp_dict[tmp_key]
            tmp_dict[key.split("/")[-1]] = value
        return ret_dict



input_json = '''{ "Id": "101",
"header": {"funcNo": "IF01",
"mobile":"075512344565"},
 "payload": {"contact": [{
			"mobile": "123456789999",
			"wechat": "test"}] }}
'''
key_list =["/header/mobile","/payload/contact/0/mobile","/Id"]
value_list=["2222222", "111111111", "100"]


print(Solutions.func(input_json, key_list, value_list))

