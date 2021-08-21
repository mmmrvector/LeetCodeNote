# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        dp = [[] for _ in range(len(ss))]
        dp[0] = [ss[0]]
        for i in range(1, len(ss)):
            for s in dp[i - 1]:
                for j in range(len(s)):
                    if ss[i] == s[j]:
                        continue
                    dp[i].append(s[:j] + ss[i] + s[j:])
                dp[i].append(s + ss[i])
        return sorted(dp[len(ss) - 1])
