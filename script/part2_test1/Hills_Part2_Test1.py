# coding=utf-8
__author__ = 'hillszhang'


class Part2():

    def __init__(self):
        pass

    @staticmethod
    def Test2(inputStr):
        """
        计算字符串个数和字符类别

        :param string inputStr: 输入的待分析语句
        :return [int num, dict my_dict ]:字符个数，字符种类个数
        """

        result = {}
        num = 0
        for c in inputStr:
            if c.isalnum() or c == "_":
                if not result.has_key(c):
                    result[c] = 1
                    num += 1
                else:
                    result[c] += 1
        return num, result


if __name__ == "__main__":
    s = "We are fasdasdfasdfadf2q341234adf,./,/ipmissy1122¡ª_.hello my name is ruby12jlksjdflsjfljslfjlsj1"
    print Part2.Test2(s)
