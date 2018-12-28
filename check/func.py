#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Auto check function library
"""
# import the system module
import datetime
import logging
import os
import traceback

# import the check config
import check_data

"""
    Project config
"""
# 1. Path config, automatic generation based on environment
QUESTION_PREFIX = check_data.CFG_QUES_NUMBER
PATH_FUNC_FILE = CASE_PATH = str(os.path.abspath(__file__))
PATH_PROJECT = PATH_FUNC_FILE.split(os.sep + "check" + os.sep + "func.py")[0]
PATH_SCRIPT = PATH_PROJECT + os.sep + "script" + os.sep + QUESTION_PREFIX.lower()

# 2. File config
PATH_LOG_FILE = PATH_PROJECT + os.sep + "log" + os.sep + "check.log"
PATH_RESULT_FILE = PATH_PROJECT + os.sep + "result" + os.sep + "result.csv"
PATH_CHECK_FILE = PATH_PROJECT + os.sep + "result" + os.sep + "check_file"
PATH_CHECK_SCRIPT_FILE = PATH_PROJECT + os.sep + "check" + os.sep + "skill_script.py"
PATH_AUTO_CHECK_FILE = PATH_PROJECT + os.sep + "check" + os.sep + "auto_check.py"

# 3. Log config
LOG_FILE_MODE = "a"

# If you want to run in bulk, you need to close the log.
LOG_IS_PRINT = False

# Run Times
RUN_TIMES = 1


# --------------------------------------------------------------------------

class FuncLib:
    """
    Auto check class
    """

    def __init__(self, ):
        self.__doc__ = "This class is used to check the skill test script"

    @staticmethod
    def save_log(str_info, b_print_log=LOG_IS_PRINT):
        """
        Write the information in the log file

        :param str_info: The log information
        :param b_print_log: The screen print log switch
        :return: None
        """
        try:
            # 1. Get the path which is not include the file name
            file_dir = os.path.split(PATH_LOG_FILE)[0]
            # If the log path does not exist, create the path recursively
            if not os.path.isdir(file_dir):
                os.makedirs(file_dir, 0775)

            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(levelname)s : %(message)s',
                                filemode=LOG_FILE_MODE,
                                filename=PATH_LOG_FILE)

            if b_print_log:
                console = logging.StreamHandler()  # define console handler
                console.setLevel(logging.DEBUG)  # define the leave of thishandler
                # Can't get the line number of the execution line
                formatter = logging.Formatter('%(asctime)s %(levelname)s : %(message)s')  # define the format of the log string
                console.setFormatter(formatter)
                # Create an instance
                logging.getLogger().addHandler(console)
                logging.debug(str_info)
                # Solve the problem of repetition
                logging.getLogger().removeHandler(console)
            else:
                # The purpose of the separate write here is to delete the handle when the terminal outputs,
                # to prevent repeated printing
                logging.debug(str_info)
        except Exception as e:
            print str("ssss" + e.message)
            traceback.print_exc()
            pass

    def format_err(self, err_obj):
        """
        Check the error message. If the length of the error message is zero, return the error message "Unknown error".

        :param err_obj: The error object.
        :return: The formatted error message string.
        """
        try:
            return "Unknown error" if len(str(err_obj.message)) == 0 else str(err_obj.message)
        except Exception as e:
            self.save_log("The object error is invalid, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())
            return "Unknown error"

    def get_script_summary(self):
        """
        Read the check_file to generate script profile information

        :return: the summary dict
        """
        dict_csv_result = {
            "name": "",
            "part_index": "",
            "test_index": ""
        }
        try:
            with open(PATH_CHECK_FILE) as f:
                str_script_summary = f.readline()
                list_script_summary = str_script_summary.lower().split("_")
                if len(list_script_summary) > 2:
                    dict_csv_result["name"] = list_script_summary[0]
                    dict_csv_result["part_index"] = list_script_summary[1]
                    dict_csv_result["test_index"] = list_script_summary[2]
        except Exception as e:
            self.save_log("Get the script summary failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())
        return dict_csv_result

    def save_result(self, **kwargs):
        """
        Program test completed, store execution results

        :param kwargs: the result information
        :return: None
        """

        try:
            list_keys = ["name", "part_index", "test_index", "result", "time", "list_result", "info"]
            if not all(map(kwargs.has_key, list_keys)):
                self.save_log("Err02: result dictionary is invalid.")
                self.save_log("Desired keys: {excepted_keys}".format(excepted_keys=list_keys))
                self.save_log("Actual  keys: {real_keys}".format(real_keys=kwargs.keys()))
                # return None
            with open(PATH_RESULT_FILE, "a") as f:
                f.write(" {name}, {part_index}, {test_index}, {result}, {time}, {list_result}, {info} \n".format(**kwargs))
        except Exception as e:
            self.save_log("Err01: save result failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

    def write_col_name(self):
        """
        Write the column name

        :return: None
        """
        try:
            dict_csv_result = {
                "name": "Name",
                "part_index": "Part number",
                "test_index": "Test number",
                "result": "Script result",
                "time": "Average time(μs)",
                "list_result": "Each item result",
                "info": "Each item return data"
            }
            self.save_result(**dict_csv_result)
            self.save_log("Write the column name in csv result file, column:{result}".format(result=dict_csv_result))
            pass
        except Exception as e:
            self.save_log("Write the column name of the csv result failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

    def get_class(self, obj_module):
        """
        Gets all the classes of the test script

        :param obj_module: The module object
        :return: the list of the class
        """
        list_class = [method for method in dir(obj_module) if callable(getattr(obj_module, method))]
        self.save_log("Get the classes of the test script, class list: {list_class}".format(list_class=list_class))
        return list_class

    def call_function(self, obj_class, *args):
        """
        Automatic test function

        :param obj_class: The test class name
        :param args: Input parameters of the function to be tested. It's type is a list of the input parameters' value
        :return:  Function run results and execution times
        """
        # Record start time
        list_func_result, i_exe_time = [], 1000000000
        try:
            begin = datetime.datetime.now()
            self.save_log("Start check class: {class_name}, start time: {begin}".format(class_name=obj_class, begin=begin))

            list_func_result = []
            for index, value in enumerate(dir(obj_class)):
                if not value.startswith("_"):
                    method_function = getattr(obj_class, value, lambda: "nothing")
                    obj_result = method_function(*args)
                    list_func_result.append(obj_result)

            # Record end time
            end = datetime.datetime.now()
            # Computation execution time, in microseconds
            i_exe_time = (end - begin).total_seconds() * 1000000
            self.save_log("Finish check class, result: {result}, end time: {end}".format(result=list_func_result, end=end))
            self.save_log("Execution time: {exe_time}".format(exe_time=i_exe_time))
        except Exception as e:
            self.save_log("Call function failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

        return list_func_result, i_exe_time

    def get_check_config(self):
        """
        Get the detection configuration according to the topic configuration.
        Includes input parameters and expected output results.

        :return: The list of input parameters and excepted value
        """
        list_check_data, list_excepted_result = [], []
        try:
            # Get all the check config
            list_var = dir(check_data)

            # Question number prefix
            str_quest_prefix = check_data.CFG_QUES_NUMBER

            for index, value in enumerate(list_var):
                if value.startswith(str_quest_prefix + "_list_check"):
                    list_check_data = getattr(check_data, value)

                if value.startswith(str_quest_prefix + "_list_excepted"):
                    list_excepted_result = getattr(check_data, value)
        except Exception as e:
            self.save_log("Get check config failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())
        self.save_log("Get config,   check_data: {data}".format(data=list_check_data))
        self.save_log("Get config, check_result: {result}".format(result=list_excepted_result))
        return list_check_data, list_excepted_result

    def check_return_result(self, input_para, return_result, excepted_result, check_type=check_data.CHECK_TYPE):
        """
        Compare the results returned with the expected results according to the type of check

        :param input_para: The input parameters' values
        :param return_result: The test class returned result
        :param excepted_result: Expected results in the configuration file
        :param check_type: The check type, default check_type is EQUAL
        :return: the bool check result
        """
        bool_result = True
        try:

            # 1. Default check type
            if check_type.upper() == "EQUAL":
                self.save_log("Return   data: " + str(return_result))
                self.save_log("excepted data: " + str(excepted_result))
                if return_result == excepted_result:
                    bool_result = True
                else:
                    bool_result = False
                self.save_log("Check type: equal.")
                self.save_log("Check result: {result}.".format(result=bool_result))

            # 2. Part3_Test1 check function
            if check_type.upper() == "PART3_TEST1":
                bool_result = self.test_method_part3_test1(input_para, return_result, excepted_result)
                self.save_log("check_return_result function check result: {result}".format(result=bool_result))
        except Exception as e:
            self.save_log("Get check config failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())
        return bool_result

    # -----------------------------------------------------------------------------------------------------------
    # User-defined test method
    def test_method_part3_test1(self, input_para, return_result, excepted_result=""):
        """
        Part3 test1 detection function

        :param input_para: The input parameters' value
        :param return_result: The return result
        :param excepted_result: The excepted value
        :return: the bool result
        """
        b_result = False
        self.save_log("Input para: {input_para}".format(input_para=input_para))
        self.save_log("Return data: {return_data}".format(return_data=return_result))
        self.save_log("Except data: {except_data}".format(except_data=excepted_result))
        try:
            i_range, i_number, list_scope = input_para[0], input_para[1], input_para[2]
            list_source, list_cmp, i_len = return_result[0]
            list_source.sort()
            list_cmp.sort()

            # 1. Check range array range is correct
            check_source = [i for i in list_source if 0 <= i <= i_range]
            b_check_source = sorted(check_source) == list_source
            self.save_log("Check that the range of the first return data is correct, result: {result}".format(
                result=b_check_source))

            # 2. Check that the range array is a subset of random arrays
            b_check_scope = True if len(list(set(list_cmp).difference(set(list_source)))) == 0 else False

            # 3. Check that the range array is correct
            list_except = [i for i in list_source if list_scope[0] <= i <= list_scope[1]]
            b_check_cmp = sorted(list_cmp) == sorted(list_except)
            self.save_log(str(sorted(list_cmp)) + "," + str(sorted(list_except)))

            # 4. Check that the range of random arrays is correct
            list_check_range = [i for i in list_cmp if list_scope[0] <= i <= list_scope[1]]
            b_check_range = sorted(list_check_range) == list_cmp

            # 5. Check length
            b_check_len = i_len == len(list_cmp)
            self.save_log("Check scope length: {len}".format(len=b_check_len))
            b_check_first_len = len(list_source) == i_number

            list_result = [b_check_source, b_check_scope, b_check_cmp, b_check_range, b_check_len, b_check_first_len]
            self.save_log("Item result: {result}".format(result=list_result))
            b_result = all(list_result)
            self.save_log("test_method_part3_test1 function check result: {result}".format(result=b_result))
        except Exception as e:
            b_result = False
            self.save_log("Call test_method_part3_test1 failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

        return b_result
