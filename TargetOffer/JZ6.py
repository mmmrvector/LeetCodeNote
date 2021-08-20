# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here

        if len(rotateArray) == 0:
            return 0
        # brute force
        # min_val = 10** 8
        # for a in rotateArray:
        #     min_val = min(min_val, a)
        # return min_val

        # binary search
        start = 0
        end = len(rotateArray) - 1
        while start < end:
            if rotateArray[start] < rotateArray[end]:
                return rotateArray[start]
            mid = int((start + end) / 2)
            if rotateArray[mid] > rotateArray[end]:
                start = mid + 1
            elif rotateArray[mid] < rotateArray[end]:
                end = mid
            else:
                end -= 1
        return rotateArray[start]