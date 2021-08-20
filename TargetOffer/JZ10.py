# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        dp = [0] * max(number,2)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, number):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number - 1]
