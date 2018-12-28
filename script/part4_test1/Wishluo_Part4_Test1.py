# -*- coding:utf-8 -*-


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def test(x):
        i = 0
        find_str = x[0]
        len_str = len(find_str)
        while i <= len_str:
            for tmp in x:
                if len(tmp) < i+1:
                    return x[0][0:i]
                elif not(tmp[i] == find_str[i]):
                    return x[0][0:i]
            i = i+1


if __name__ == "__main__":
    ls = ['apple', 'append', 'app']
    ls1 = ['apple', '', 'app']  # 返回空串
    ls2 = ['', 'append', 'app']  # 返回空串
    ls3 = ['', '', '']
    obj1 = Solution()
    print obj1.test(ls)
    if obj1.test(ls1) == '':
        print 'OK'

