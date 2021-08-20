# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1:
            return 1
        dp = [0] * number
        dp[0] = 1
        dp[1] = 2
        for i in range(2, number):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number - 1]
