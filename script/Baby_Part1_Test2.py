# encoding:utf-8
import copy


class EqualZero:

    def __init__(self):
        self.__doc__ = "This is number test"
        self.__author = "Babyzheng"

    @staticmethod
    def equal0(arr=[]):

        """
        Given one list arr[],when the three values are added to 0, the list is returned.
        :param arr: list
        :return:the list result
        """
        new_s = []
        # 列表长度<3 返回
        if len(arr) < 3:
            return -1
        # 先把数组进行排序
        arr.sort()
        # 外层循环
        for i in range(0, len(arr)-1):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            m = i + 1
            n = len(arr) - 1
            while m < n:
                if arr[i] + arr[m] + arr[n] < 0:
                    m = m + 1
                elif arr[i] + arr[m] + arr[n] > 0:
                    n = n - 1
                # 三个元素相加和为零
                else:
                    tmp_arr = []
                    tmp_arr.append(arr[i])
                    tmp_arr.append(arr[m])
                    tmp_arr.append(arr[n])
                    num_tuple = tuple(tmp_arr)
                    new_s.append(num_tuple)
                    # result = list(set(result))
                    # new_s.sort()
                    m = m + 1
                    n = n - 1
        result = []
        for x in new_s:
            if x not in result:
                result.append(x)
        return result


# print EqualZero.equal0(arr=[0, 0, 0, 0, -1, 1, -2, 1])








