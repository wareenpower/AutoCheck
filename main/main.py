#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   The main programme of the AUTO-CHECK project
"""
import func

clib = func.FuncLib()

LOG_MAIN_FLAG = True

if __name__ == "__main__":
    clib.save_log("==================================================================================================", LOG_MAIN_FLAG)
    # 1. Gets a list of script files with the specified title number
    list_script = clib.get_script_list()

    # 2. Check if the script file exists
    if not list_script:
        clib.save_log("Failed to search for a script that meets the criteria, the program exits", LOG_MAIN_FLAG)
        exit(1)

    # 3. Clear the csv result file
    clib.save_log("--------------------------------------------------------------------------------------------------", LOG_MAIN_FLAG)
    clib.save_log("Step1. Clear file.", LOG_MAIN_FLAG)
    clib.clear_result()
    clib.write_col_name()

    # 4. Start check
    clib.save_log("--------------------------------------------------------------------------------------------------", LOG_MAIN_FLAG)
    clib.save_log("Step2. Start check.", LOG_MAIN_FLAG)
    clib.save_log("Total script number: {number}".format(number=len(list_script)), LOG_MAIN_FLAG)
    for index, script_file in enumerate(list_script):
        clib.save_log("**************************************************************************************************", LOG_MAIN_FLAG)
        clib.save_log("Check index: {index}, script path:{script_path}".format(index=index+1, script_path=script_file), LOG_MAIN_FLAG)
        clib.run_script(script_file)

    # 5. backup the csv result file
    clib.save_log("--------------------------------------------------------------------------------------------------", LOG_MAIN_FLAG)
    clib.save_log("Step3. Backup result file.", LOG_MAIN_FLAG)
    clib.backup_result()
    clib.save_log("--------------------------------------------------------------------------------------------------", LOG_MAIN_FLAG)
    clib.save_log("Finish check", LOG_MAIN_FLAG)
    clib.save_log("==================================================================================================", LOG_MAIN_FLAG)
