#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter
import re


class BStringObjectTest:

    def __init__(self):
        self.__doc__ = "This is the answer for StringObjectTest in 2018-11-01 !"
        self.__author = "Junacheng"

    @staticmethod
    def compute_frequency(str_input):
        """
        Given a str str_input,return the number of distinct character it contains (space not included) and frequency of each character !

        :param str str_input: str object to test
        :return: the number of distinct character it contains (space not included) and frequency of each character !

        Example
        -------
        >>> #1. one str that contains several space
        # >>> StringObjectTest().compute_frequency("wo are you")
        # (7, {'o': 2, 'a': 1, 'e': 1, 'r': 1, 'u': 1, 'w': 1, 'y': 1})
        >>> #2. one str that contains no space
        # >>> StringObjectTest().compute_frequency("you are my super star!")
        # (10, {'r': 3, 'a': 2, 'e': 2, 's': 2, 'u': 2, 'y': 2, 'm': 1, 'o': 1, 'p': 1, 't': 1})
        """

        if not isinstance(str_input, str):
            pass

        final_str = re.sub(r"[\s+.;!/,$&%^*()<>\[\]\"\'?@|:`~{}#]+|[—！\\，。=？、：“”‘’￥…（）《》【】]", "", str_input)
        map_character_frequency = Counter(final_str)
        return len(map_character_frequency), dict(map_character_frequency)


# if __name__ == "__main__":
print BStringObjectTest.compute_frequency("We are fasdasdfasdfadf2q341234adf,./,/ipmissy1122—_.")