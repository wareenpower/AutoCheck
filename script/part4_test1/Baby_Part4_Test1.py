# encoding:utf-8


class Test4Sequence:

    def __init__(self):
        self.__doc__ = "This is string test"
        self.__author = "Baby"

    @staticmethod
    def list_common(str_input):
        """
        Find common substrings of strings
        :param str_input:The input parameter
        :return: common substrings of strings
        """
        if len(str_input) == 0:
            return ''
        elif len(str_input) == 1:
            return str_input
        str_1 = min(str_input)
        str_2 = max(str_input)
        for i, j in enumerate(str_1):
            if j != str_2[i]:
                return str_1[:i]
        return str_1


if __name__ == '__main__':
    s = Test4Sequence()
    print(s.list_common(["ower", "flow", "flight"]))
