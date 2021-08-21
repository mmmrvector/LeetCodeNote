# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n == 0:
            return 0
        def countOnes(x):
            cnt = 0
            while x / 10 != 0:
                if x % 10 == 1:
                    cnt += 1
                x = int(x / 10)
            return cnt
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + countOnes(i)
        return dp[n]