# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        res = []
        for i in range(1, tsum - 1):
            for j in range(i + 1, tsum):
                s = (i + j) * (j - i + 1) / 2
                if s == tsum:
                    res.append([x for x in range(i, j + 1)])
        return res