class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import copy
        # new_p = ""
        # for i, pp in enumerate(p):
        #     if i == 0 or (p[i] != p[i - 1]) or(p[i] == p[i - 1] and p[i] != "*"):
        #         new_p += pp
        # p = new_p
        # memo = {}
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n + 1)] for __ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m):
            dp[i][0] = False
        for i in range(m + 1):
            for j in range(1, n + 1):
                if i == 0:
                    if p[j - 1] == "*":
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = False
                else:
                    if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                        dp[i][j] = dp[i - 1][j - 1]
                        continue
                    if p[j - 1] == '*':
                        if dp[i - 1][j] or dp[i][j - 1]:
                            dp[i][j] = True
                    else:
                        dp[i][j] = False

        return dp[m][n]



s = Solution()
#print(s.isMatch("abcabczzzde","*abc???de*"))
print(s.isMatch("baaaababbbaabbbbabbababaababaaabaababbbaabaabbbbaabbbbbbaabaabbababaaaaaaaabbbaaabbbababbbbbabbbbabbbbabbaabaababababbbababbbbbbbaaaaabbbbabbbbbaabbbaaaabaaabbabbabaabbbbabbbabbbaababbabbaaaababbababa","*bb*abb*a**ba**aba*b*bbb*abbaaa*bb*b**a*b*b**a**abb***ab*b**b*b*a******a*a*babaa*bab*a*b****bb*babb*baa"))