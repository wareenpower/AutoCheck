# -*- coding:utf-8 -*-
import json


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def test(x, y, z):                     #x:字符串  y:list  z:list
        re_dict = json.loads(x)
        tmp = re_dict
        len_of_y = len(y)
        i = 0
        j = 0
        while (i < len_of_y):
            test = y[i]
            key_list = test.split('/')           #将字符串转换为列表
            len_of_key = len(key_list)
            while (j < (len_of_key - 1)):
                if key_list[j] == '':                    #以/分割后，第一个字符串为''
                    j = j + 1
                    continue
                elif not(key_list[j].isdigit()):
                    tmp = tmp[key_list[j]]
                    j = j + 1
                else:
                    index = int(key_list[j])
                    tmp = tmp[index]
                    j = j + 1
            tmp[key_list[j]] = z[i]
            i = i+1
            j = 0
            tmp = re_dict
        return re_dict


if __name__ == "__main__":
    jason_str ='''{"eventId":101,"interface":{"para":{"id":"g514","rules":[{"name":"test1","type":"digest"}],"users":[{"user":"tdsql@%","type":"deny","match":"any","rules":[{"name":"test1","type":"digest"}]}]}}}'''
    key_test = ["/interface/para/users/0/rules/0/name", "/interface/para/rules/0/type", "/eventId"]
    value_test = ["myname", "mytype", 100]
    re = {'eventId': 100, 'interface': {'para': {'rules': [{'type': 'mytype', 'name': 'test1'}], 'id': 'g514', 'users': [
        {'rules': [{'type': 'digest', 'name': 'myname'}], 'type': 'deny', 'user': 'tdsql@%', 'match': 'any'}]}}}
    obj1 = Solution()
    print obj1.test(jason_str,key_test,value_test)

    print obj1.test(jason_str,key_test,value_test)==re