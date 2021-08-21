# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        res = {}
        for a in numbers:
            if a not in res:
                res[a] = 1
            else:
                res[a] += 1
        for key in res:
            if res[key] > len(numbers) / 2:
                return key