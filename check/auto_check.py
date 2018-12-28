#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    Auto check script programme
"""
import time
# System module
import traceback

import check_data
# User's module
import func
# import test module
import skill_script as test_module

# --------------------------------------------------------------------------------
"""
    Check parameter legitimacy
"""
# Instantiation class
clib = func.FuncLib()

LOG_CHECK_SUMMARY_PRINT_FLAG = True

try:
    # Get the classes of the test script
    list_class = clib.get_class(test_module)
    if not list_class:
        clib.save_log("There are no callable classes in the test script", LOG_CHECK_SUMMARY_PRINT_FLAG)
        exit(1)

    # Get input parameters and expected results based on the test data configuration
    list_check_data, list_excepted_result = clib.get_check_config()

    if len(list_check_data) != len(list_excepted_result):
        clib.save_log("Check data or excepted result is invalid.", LOG_CHECK_SUMMARY_PRINT_FLAG)
    # --------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------
    """
        Call function for loop validation
    """
    # Get the first class by default. If multiple class algorithms are provided, subsequent extensions into for loops
    class_name = getattr(test_module, list_class[0], lambda: "nothing")

    # Define the parameter used to save the result and the time
    list_all_ret_result, list_ret_time = [], []
    i_total_time = 0

    list_check_result = []

    for i_time in range(func.RUN_TIMES):
        clib.save_log("====================================================================================", LOG_CHECK_SUMMARY_PRINT_FLAG)
        clib.save_log("Check time: {time_number}".format(time_number=i_time+1), LOG_CHECK_SUMMARY_PRINT_FLAG)
        for index, value in enumerate(list_check_data):
            # 1. Run the program to check
            clib.save_log("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++", LOG_CHECK_SUMMARY_PRINT_FLAG)
            clib.save_log("Check data index: {index}".format(index=index+1), LOG_CHECK_SUMMARY_PRINT_FLAG)
            clib.save_log("Check  data: {data}".format(data=value))
            list_return_result, i_exe_time = clib.call_function(class_name, *value)
            clib.save_log("Return data: {result}".format(result=list_return_result))
            clib.save_log("Execution time: {exe_time}".format(exe_time=i_exe_time), LOG_CHECK_SUMMARY_PRINT_FLAG)

            list_all_ret_result.append(list_return_result)
            list_ret_time.append(i_exe_time)
            i_total_time += i_exe_time

            # 2. Check the return result
            b_result = clib.check_return_result(value, list_return_result, list_excepted_result[index])
            list_check_result.append(b_result)
            clib.save_log("Check result: {result}".format(result=b_result), LOG_CHECK_SUMMARY_PRINT_FLAG)
            clib.save_log("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            time.sleep(0.001)

    i_avg_time = i_total_time // len(list_check_result)
    # Json summary result
    dict_result = {
        "data": {
            "input": list_check_data,
            "output": list_all_ret_result,
            "excepted": list_excepted_result
        },
        "result": {
            "item_result": list_check_result,
            "check_result": all(list_check_result)
        },
        "time": {
            "total": i_total_time,
            "avg_time": i_avg_time
        }
    }

    # CSV Result dict
    clib.save_log("************************************************************************************", LOG_CHECK_SUMMARY_PRINT_FLAG)
    # list_keys = ["name", "part_index", "test_index", "result", "time", "list_result", "info"]
    dict_csv_result = {
        "name": "",
        "part_index": "",
        "test_index": "",
        "result": "",
        "time": "",
        "list_result": "",
        "info": ""
    }
    dict_script_summary = clib.get_script_summary()
    dict_csv_result.update(dict_script_summary)
    dict_csv_result["result"] = all(list_check_result)
    dict_csv_result["time"] = i_avg_time
    dict_csv_result["list_result"] = str(list_check_result).replace(",", ";")
    if check_data.SAVE_RETURN_DATA:
        dict_csv_result["info"] = "return data:{data}".format(data=list_all_ret_result).replace(",", ";")
    else:
        dict_csv_result["info"] = "Nothing"

    clib.save_log("Save result to csv file", LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Result dict: {dict_result}".format(dict_result=dict_csv_result))
    clib.save_result(**dict_csv_result)

    clib.save_log("************************************************************************************", LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Complete verification, summary information:", LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Input  data: {input}".format(input=list_check_data))
    clib.save_log("Output data: {output}".format(output=list_all_ret_result))
    clib.save_log("Excepted data: {excepted}".format(excepted=list_excepted_result))
    clib.save_log("Each item check result: {item_result}".format(item_result=list_check_result), LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Check  result: {excepted}".format(excepted=all(list_check_result)), LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Total execution time: {total_time}".format(total_time=i_total_time), LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Function running average time: {exe_time}".format(exe_time=i_avg_time), LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("Summary JSON: {json}".format(json=dict_result))
    clib.save_log("Finish check.", LOG_CHECK_SUMMARY_PRINT_FLAG)
    clib.save_log("************************************************************************************", LOG_CHECK_SUMMARY_PRINT_FLAG)
except Exception as e:
    clib.save_log("Err: {err}".format(err=str(e.message)))
    clib.save_log(traceback.format_exc())
