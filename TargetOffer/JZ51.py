# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        dp = [1 for _ in A]
        for i in range(1, n):
            dp[0] = dp[0] * A[i]
        for i in range(1, n):
            if A[i] == 0:
                for j in range(n):
                    if j != i:
                        dp[i] = dp[i] * A[j]
            else:
                dp[i] = int(dp[i - 1] * A[i - 1] / A[i])
        return dp
s = Solution()
print(s.multiply([1,2,3,4,5]))