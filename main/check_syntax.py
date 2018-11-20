#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
   The main programme of the AUTO-CHECK project
"""
import func

clib = func.FuncLib()
CHECK_SYNTAX_LOG_FLAG = True

if __name__ == "__main__":
    clib.save_log("==================================================================================================", CHECK_SYNTAX_LOG_FLAG)
    # 1. Gets a list of xml syntax files with the specified title number
    list_syntax_xml = clib.get_syntax_files()

    # 2. Check if the script file exists
    if not list_syntax_xml:
        clib.save_log("Failed to search for a script that meets the criteria, the program exits", CHECK_SYNTAX_LOG_FLAG)
        clib.save_log("==================================================================================================", CHECK_SYNTAX_LOG_FLAG)
        exit(1)

    # 3. Get the file result
    dict_result = {}
    for index, xml_file in enumerate(list_syntax_xml):
        clib.save_log("**************************************************************************************************", CHECK_SYNTAX_LOG_FLAG)
        clib.save_log("Check index: {index}, xml path: {script_path}".format(index=index+1, script_path=xml_file), CHECK_SYNTAX_LOG_FLAG)
        clib.xml_read(xml_file, dict_result)
    clib.save_log("Check result: {result}.".format(result=dict_result))

    # 4. Save result and calculate score
    clib.save_xml_result(dict_result)

    # 5. Result ranking
    clib.backup_syntax_result()

    clib.save_log("Finish check", CHECK_SYNTAX_LOG_FLAG)
    clib.save_log("==================================================================================================", CHECK_SYNTAX_LOG_FLAG)
