# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        res = {}
        for i, ss in enumerate(s):
            if ss not in res:
                res[ss] = [1, i]
            else:
                res[ss][0] += 1
        for key in res:
            if res[key][0] == 1:
                return res[key][1]
        return -1