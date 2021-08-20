# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        dp = [1]
        for i in range(1, number):
            dp.append(0)
            for j in range(i):
                dp[i] += dp[j]
            dp[i] += 1
        return dp[number - 1]