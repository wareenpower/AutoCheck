
dict_info = {
    "1": 2
}

print dict_info
["./check_file/p7_t1/file1.txt", "./check_file/p7_t1/file2.txt"]

# import pandas as pd
#
# df = pd.read_csv("result.csv")
# df.sort_values(by=["Script_result", "AvgTime"], ascending=[False, True], inplace=True)
# df['Index'] = range(1, len(df)+1)
# df = df.set_index('Index')
# df.to_csv("1.csv")
# print(df)
#
# import numpy as np
#
# print np.random.randint(0, 100, 10)

# def get_value():
#
#     return [1, 2, 3], 2, 3
#
#
# t1, t2, t3 = get_value()
#
# print t1, t2, t3

# import os
# str_path = "file://$PROJECT_DIR$/script/zukizhu_Part1_Test2.py"
# print os.path.basename(str_path)
# print os.path.dirname(str_path)

# print (19 * 10.0) / 20
#
# z1 =  1 / 2
# print z1
#
# print all([True, True, True, True, False, True])
#
# print ''.join("info")
#
#
# str_dict_info = """{
#                 "name": "skill_test",
#                 "detail": {
#                     "part": 5,
#                     "test": {
#                         "title": "modify the dictionary key's value",
#                         "date": "2018-11-17",
#                         "temp": {
#                             "p1": 12
#                         }
#                     }
#                 },
#                 "list_1": [
#                     {"name": "part1"},
#                     {"name": "part2"}
#                 ],
#                 "int_key": {
#                     "name": "int",
#                     "0": 1
#                 }
#             }"""
#
# print type(str_dict_info)

#
# def yhTriangle(n):
#     l, index = [1], 0
#     while index < n:
#         yield l
#         l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
#         index += 1
#
# for x in yhTriangle(10):
#     print(x)

# encoding:utf-8
# import json
#
# class Test5Dict:
#
#     def __init__(self):
#         self.__doc__ = "This is dict test"
#         self.__author = "Baby"
#
#     @staticmethod
#     def edit_json_node(json_data, key, value):
#
#         key_ = key.lstrip('/').split("/")
#         key_length = len(key_)
#         i = 0
#         # scope = json.loads(json_data)
#         scope=json_data
#         while i < key_length:
#             if i + 1 == key_length:
#                 scope[key_[i]] = value
#                 i = i + 1
#             else:
#                 if key_[i].isdigit():
#                     scope = scope[int(key_[i])]
#                 else:
#                     scope = scope[key_[i]]
#                 i = i + 1
#
#         return json_data
#
#     @staticmethod
#     def edit_json_array(input_json, key_list, value_list):
#         finish_data=json.loads(input_json)
#         # finish_data = input_json
#         if len(key_list) != len(value_list):
#             return ""
#         i = 0
#         while i < len(key_list):
#             input_json = Test5Dict().edit_json_node(finish_data,key_list[i], value_list[i])
#             i = i + 1
#         # finish_data=json.dumps(input_json)
#         return finish_data
#
#
# if __name__ == '__main__':
#     # input_ = {"Id": "101",
#     #               "header": {"funcNo": "IF01",
#     #                          "mobile": "075512344565"},
#     #               "payload": {"contact": [{
#     #                   "mobile": "123456789999",
#     #                   "wechat": "test"}]}}
#     # key_2 = ["/header/mobile", "/payload/contact/0/mobile", "/Id"]
#     # value_ = ["0755 839699", "13546467885", "100"]
#
#
#     input_ = '''{"eventId":101,"interface":{"para":{"id":"g514","rules":[{"name":"test1","type":"digest"}],
#                   "users":[{"user":"tdsql@%","type":"deny","match":"any",
#                   "rules":[{"name":"test1","type":"digest"}]}]}}}'''
#     key_2 = ["/interface/para/users/0/rules/0/name","/interface/para/rules/0/type","/eventId"]
#     value_ = ["myname","mytype", 100]
#
#
#     a = Test5Dict()
#     b = a.edit_json_array(input_, key_2, value_)
#     print type(b)
#     print b

