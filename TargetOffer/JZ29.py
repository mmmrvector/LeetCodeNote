# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k == 0:
            return []
        tinput = sorted(tinput)
        return tinput[:k]