# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == 0:
            return 0
        # write code here
        res = [1]
        next1 = [2]
        next2 = [3]
        next3 = [5]
        idx1, idx2, idx3 = 1, 1, 1
        for i in range(1, index):
            mv = min(next1[-1], next2[-1], next3[-1])
            res.append(mv)
            if mv == next1[-1]:
                next1.append(res[idx1] * 2)
                idx1 += 1
            if mv == next2[-1]:
                next2.append(res[idx2] * 3)
                idx2 += 1
            if mv == next3[-1]:
                next3.append(res[idx3] * 5)
                idx3 += 1
        return res[-1]