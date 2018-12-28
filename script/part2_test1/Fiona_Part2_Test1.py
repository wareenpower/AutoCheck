#!/usr/bin/env python
# -*- coding:utf-8 *

import re

class StrCount:
    def __init__(self):
        self.__doc__ = 'training Part2_Test1'
        self.__author = 'Fionazhan'

    @staticmethod
    def count_(str_para):
        d = {}
        strme = re.sub("\W","",str_para)
        #print strme
        for key in strme:
            #d.update({str(key):strme.count(key)})
            d[str(key)] = strme.count(key)
        return len(d),d

#a = StrCount

#print a.count_("We are fasdasdfasdfadf2q341234adf,./,/ipmissy1122—_.hello my name is ruby12jlksjdflsjfljslfjlsj1")
