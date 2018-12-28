#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import datetime


class Part7Test1Solution:

    def __init__(self):
        self.__doc__ = "part7 test1 answer"

    @staticmethod
    def calc_data_by_filter(str_src_file_path):
        user_avg = 0
        io_wait_count = 0
        try:
            # 读取数据，跳过第一行和第二行，使用多空格进行分割
            df_data = pd.read_csv(str_src_file_path, skiprows=[0, 1], delim_whitespace=True, engine='c')

            # 设置索引列，非必须步骤，只是看上去舒服一点
            df_data['Index'] = range(1, len(df_data) + 1)
            df_data = df_data.set_index('Index')

            list_column_name = df_data.columns.values.tolist()
            # 修改列名，时间的列名看上去不太美观，修改为字符
            df_data.rename(columns={list_column_name[0]: 'Time'}, inplace=True)

            # 过滤列名，去除average，需要先后去列表，然后去除列表，最后使用isin进行重新修改DataFrame
            list_time = list(df_data['Time'])
            # 可能不存在Average: 一行，需要判断
            if 'Average:' in list_time:
                list_time.remove('Average:')
            df_data = df_data[df_data['Time'].isin(list_time)]
            # --------------------------------------------------------------------------------------
            # 调试生成测试数据
            # df_data.to_csv(str_src_file_path + "_all_detail")
            # --------------------------------------------------------------------------------------

            # 按照system过滤达到新的df
            df_new_user_avg = df_data[df_data['%system'] > 1.5]

            # --------------------------------------------------------------------------------------
            # 调试生成测试数据
            # df_new_user_avg.to_csv(str_src_file_path + "_user_avg_detail")
            # --------------------------------------------------------------------------------------

            # 计算所有列的平均值
            avg_result = df_new_user_avg.mean()
            # 获取user的平均值
            user_avg = avg_result["%user"]

            # 如果没有满足条件的，计算出来的会为nan，需要判断，恢复默认
            if np.isnan(user_avg):
                user_avg = 0

            # 根据iowait过滤
            df_io_wait_count = df_data[df_data['%iowait'] > 0.12]

            # --------------------------------------------------------------------------------------
            # 调试生成测试数据
            # df_io_wait_count.to_csv(str_src_file_path + "_io_wait_detail")
            # --------------------------------------------------------------------------------------

            # 获取长度就是总数
            io_wait_count = len(df_io_wait_count)
        except Exception as e:
            print e.message
        return round(user_avg, 6), io_wait_count


if __name__ == "__main__":
    begin = datetime.datetime.now()
    str_input = "./check_file/file7.txt"
    print Part7Test1Solution().calc_data_by_filter(str_input)
    end = datetime.datetime.now()
    print (end - begin).total_seconds() * 1000000
