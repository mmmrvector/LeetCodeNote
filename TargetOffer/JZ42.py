# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        end = len(array) - 1
        for i in range(len(array) - 1):
            for j in range(end,  i , -1):
                if array[i] + array[j] == tsum:
                    if not res or array[i] * array[j] < res[0] * res[1]:
                        res = [array[i], array[j]]
                        end = j - 1
                        break
        return res

