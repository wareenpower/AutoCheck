# encoding:utf-8
import json


class Test5Dict:

    def __init__(self):
        self.__doc__ = "This is dict test"
        self.__author = "Baby"

    @staticmethod
    def _edit_json_node(json_data, key, value):

        key_ = key.lstrip('/').split("/")
        key_length = len(key_)
        i = 0

        scope = json_data
        while i < key_length:
            if i + 1 == key_length:
                scope[key_[i]] = value
                i = i + 1
            else:
                if key_[i].isdigit():
                    scope = scope[int(key_[i])]
                else:
                    scope = scope[key_[i]]
                i = i + 1

        return json_data

    @staticmethod
    def edit_json_array(input_json, key_list, value_list):
        finish_data = json.loads(input_json)

        if len(key_list) != len(value_list):
            return ""
        i = 0
        while i < len(key_list):
            finish_data = Test5Dict()._edit_json_node(finish_data, key_list[i], value_list[i])
            i = i + 1

        return finish_data


# if __name__ == '__main__':
#     input_ = {"Id": "101",
#                   "header": {"funcNo": "IF01",
#                              "mobile": "075512344565"},
#                   "payload": {"contact": [{
#                       "mobile": "123456789999",
#                       "wechat": "test"}]}}
#     key_2 = ["/header/mobile", "/payload/contact/0/mobile", "/Id"]
#     value_ = ["0755 839699", "13546467885", "100"]
#
#
#     input_ = '''{"eventId":101,"interface":{"para":{"id":"g514","rules":[{"name":"test1","type":"digest"}],
#                   "users":[{"user":"tdsql@%","type":"deny","match":"any",
#                   "rules":[{"name":"test1","type":"digest"}]}]}}}'''
#     key_2 = ["/interface/para/users/0/rules/0/name","/interface/para/rules/0/type","/eventId"]
#     value_ = ["myname","mytype", 100]
#
#     # input_ = '''{ "spec": [{"cpu": 2400},{"1": [{"dir": "/data1/tdsql/data"}, {"2": [ {"b": "b1"},{"3": [{"c": "c1"},
#     #                 {"4": [ {"d": "d1"},{"5": [{"0": "e1"},  {"e1": "e1"}] } ]  }] }]}]}],"66":"test" }'''
#     #
#     # key_2 = ["/spec/1/1/1/2/1/3/1/4/1/5/0/0", "/66"]
#     # value_ = ["00", "66"]
#
#
#
#     a = Test5Dict()
#     b = a.edit_json_array(input_, key_2, value_)
#     print type(b)
#     print b
