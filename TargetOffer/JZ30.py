# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        dp = [-10 ** 9 for _ in array]
        dp[0] = array[0]
        for i in range(1, len(array)):
            dp[i] = max(dp[i - 1] + array[i], array[i])
        return max(dp)