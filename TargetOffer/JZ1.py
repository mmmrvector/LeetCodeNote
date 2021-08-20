# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        stop_col = len(array[0])
        for arr in array:
            for i, a in enumerate(arr):
                if i == stop_col:
                    break
                if a > target:
                    stop_col = i
                    break
                if a == target:
                    return True
        return False
s = Solution()
print(s.Find(3,[[1,1]]))