#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json
import re
import ast

class TestSkillSolution:

    def __init__(self):
        self.__doc__ = "This is example for skill test"
        self.__author = "fiona2"


    @staticmethod
    def json_repl(ajson,k1,v1):
        ajson = json.loads(ajson)
        for i in range(len(k1)):
            item = k1[i].replace("/","[\"",1).replace('/','"]["')+'"]'
            item = re.sub('"(\d.*?)"', r'\1',item) #FROM GUANHUA: do not need to consider dict key would be a number
            item = "ajson" + str(item) + "=" + ('"'+v1[i]+'"' if type(v1[i])!=int else str(v1[i]))
            exec(item)

        return ast.literal_eval(json.dumps(ajson))



if __name__ == "__main__":
    x = TestSkillSolution()
    ans = x.json_repl('''{"eventId":101,"interface":{"para":{"id":"g514","rules":[{"name":"test1","type":"digest"}],"users":[{"user":"tdsql@%","type":"deny","match":"any","rules":[{"name":"test1","type":"digest"}]}]}}}''', ["/interface/para/users/0/rules/0/name", "/interface/para/rules/0/type", "/eventId"], ["myname", "mytype", 100])
    print ans
    print type(ans)
#{'eventId': 100, 'interface': {'para': {'rules': [{'type': 'mytype', 'name': 'test1'}], 'id': 'g514', 'users': [{'rules': [{'type': 'digest', 'name': 'myname'}], 'type': 'deny', 'user': 'tdsql@%', 'match': 'any'}]}}}
#{'eventId': 100, 'interface': {'para': {'rules': [{'type': 'mytype', 'name': 'test1'}], 'id': 'g514', 'users': [{'rules': [{'type': 'digest', 'name': 'myname'}], 'type': 'deny', 'user': 'tdsql@%', 'match': 'any'}]}}}],
  
