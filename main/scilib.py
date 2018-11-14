##!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Scientific calculation
"""
# import the system module
import datetime

# import the scientific module
import numpy as np
import pandas as pd
import matplotlib as mp


class SciCalc():

    def __init__(self, log_path=""):
        self.__doc__ = "This class is used to scientific calc"

    def sort_result(self, file_path):
        # np.savetxt()
        pass


if __name__ == "__main__":
    start = datetime.datetime.now()

    print np.arange(20).reshape(4, 5)

    end = datetime.datetime.now()

    i_total = (end - start).total_seconds() * 1000000

    print i_total
