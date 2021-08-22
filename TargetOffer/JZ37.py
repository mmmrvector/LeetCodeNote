# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        l = 0
        r = len(data)
        while l < r:
            mid = int((l + r) / 2)
            if data[mid] < k:
                l = mid + 1
            else:
                r = mid
        lbound = l
        l = 0
        r = len(data)
        while l < r:
            mid = int((l + r) / 2)
            if data[mid] <= k:
                l = mid + 1
            else:
                r = mid
        rbound = l
        return rbound - lbound