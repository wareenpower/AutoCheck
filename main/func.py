#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Auto check function library
"""
# import the system module
import logging
import sys
import os
import shutil
import subprocess
import time
import traceback

sys.path.append('../')
from check import check_data
# --------------------------------------------------------------------------
"""
    Project config
"""

# 1. Path config, automatic generation based on environment
PATH_FUNC_FILE = CASE_PATH = str(os.path.abspath(__file__))
PATH_PROJECT = PATH_FUNC_FILE.split(os.sep + "main" + os.sep + "func.py")[0]
PATH_SCRIPT = PATH_PROJECT + os.sep + "script"

# 2. File config
PATH_LOG_FILE = PATH_PROJECT + os.sep + "log" + os.sep + "check.log"
PATH_RESULT_FILE = PATH_PROJECT + os.sep + "result" + os.sep + "result.csv"
PATH_RESULT_BACKUP_FILE = PATH_PROJECT + os.sep + "result" + os.sep + check_data.CFG_QUES_NUMBER.lower() + "_result.csv"
PATH_CHECK_FILE = PATH_PROJECT + os.sep + "result" + os.sep + "check_file"
PATH_CHECK_SCRIPT_FILE = PATH_PROJECT + os.sep + "check" + os.sep + "skill_script.py"
PATH_AUTO_CHECK_FILE = PATH_PROJECT + os.sep + "check" + os.sep + "auto_check.py"

# 3. Log config
LOG_FILE_MODE = "a"

# If you want to run in bulk, you need to close the log.
LOG_IS_PRINT = True


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

    def get_script_list(self):
        """
        Get a list of all scripts that meet the criteria

        :return: The list of script file
        """
        list_script_file = []
        try:
            # Get the question number
            str_quest_prefix = check_data.CFG_QUES_NUMBER

            for root, dirs, files in os.walk(PATH_SCRIPT):
                for file_name in files:
                    str_file_name_format = file_name.lower()
                    if str_file_name_format.endswith(str_quest_prefix.lower() + '.py'):
                        list_script_file.append(os.path.join(root, file_name))
        except Exception as e:
            self.save_log("Get script list failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())
        self.save_log("List of files that meet the criteria: {list_file}".format(list_file=list_script_file), True)
        return list_script_file

    def run_script(self, script_file):
        """
        Execute script
        1. Write the file name to the check_file
        2. auto_check read the check_file to get the title number and related information

        :param script_file: The full path of the script file
        :return:
        """
        try:
            # 1. Check if the script file exists
            if not os.path.exists(script_file):
                self.save_log("Script does not exist, file path:{file_path}".format(file_path=script_file))

            # 2. Write the file name without prefix to check_file, such as Iveshu_Part1_Test1
            with open(PATH_CHECK_FILE, "w") as f:
                f.write(os.path.splitext(os.path.split(script_file)[1])[0])

            if os.path.exists(PATH_CHECK_SCRIPT_FILE):
                os.remove(PATH_CHECK_SCRIPT_FILE)
            if os.path.exists(PATH_CHECK_SCRIPT_FILE + "c"):
                os.remove(PATH_CHECK_SCRIPT_FILE + "c")

            # 3. Copy the file to main directory and rename the script name to skill_script.py
            self.save_log("Copy script file to check, file_name: {file_name}".format(file_name=script_file), True)
            shutil.copyfile(script_file, PATH_CHECK_SCRIPT_FILE)
            time.sleep(0.001)

            # 4. Start to execute the script
            str_command = "python {check_script}".format(check_script=PATH_AUTO_CHECK_FILE)
            self.save_log("Execute script, command: {command}".format(command=str_command), True)
            self.exe_command(str_command)

        except Exception as e:
            self.save_log("Call the script function failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

    def exe_command(self, str_command):
        """
        Execute the shell command

        :param str_command: The shell command
        :return: None
        """
        try:
            p = subprocess.Popen(str_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ret_code = p.poll()
            while ret_code is None:
                ret_code = p.poll()
        except Exception as e:
            self.save_log("Execute command failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

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
                f.write("{name},{part_index},{test_index},{result},{time},{list_result},{info} \n".format(**kwargs))
        except Exception as e:
            self.save_log("Err01: save result failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

    def clear_result(self):
        """
        Delete the last remaining file before running the check

        :return: None
        """
        try:
            if os.path.exists(PATH_RESULT_FILE):
                os.remove(PATH_RESULT_FILE)
                self.save_log("Clear result, file name: {file_name}".format(file_name=PATH_RESULT_FILE), True)
        except Exception as e:
            self.save_log("clear result file failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

    def write_col_name(self):
        """
        Write the column name

        :return: None
        """
        try:
            dict_csv_result = {
                "name": "Name",
                "part_index": "Part_number",
                "test_index": "Test_number",
                "result": "Script_result",
                "time": "AvgTime",
                "list_result": "Item_result",
                "info": "Info"
            }
            self.save_result(**dict_csv_result)
            self.save_log("Write the column name in csv result file, column:{result}".format(result=dict_csv_result))
            pass
        except Exception as e:
            self.save_log("Write the column name of the csv result failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())

    def backup_result(self):
        """
        When the run is complete, rename the result file

        :return:
        """
        try:
            # 1. Clear backup csv result
            if os.path.exists(PATH_RESULT_BACKUP_FILE):
                os.remove(PATH_RESULT_BACKUP_FILE)
            if os.path.exists(PATH_RESULT_FILE):
                try:
                    import pandas as pd
                    df = pd.read_csv(PATH_RESULT_FILE)
                    df.sort_values(by=["Script_result", "AvgTime"], axis=0, ascending=[False, True], inplace=True)
                    df['Index'] = range(1, len(df) + 1)
                    df = df.set_index('Index')
                    df.to_csv(PATH_RESULT_BACKUP_FILE)
                    self.save_log("Result ranking", True)
                except Exception as e:
                    shutil.copyfile(PATH_RESULT_FILE, PATH_RESULT_BACKUP_FILE)
                    self.save_log("Err: sort failed, info: {info}".format(info=self.format_err(e)))
                self.save_log("Result file: {result_file}".format(result_file=PATH_RESULT_BACKUP_FILE), True)
        except Exception as e:
            self.save_log("Backup result file failed, info: {info}".format(info=self.format_err(e)))
            self.save_log(traceback.format_exc())
