class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # every single s of s3 is in s1 or s2

        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)
        dp = [[True for _ in range(n + 1)] for __ in range(m + 1)]

        for i in range(1, m + 1):
            r = (dp[i - 1][0] and (s1[i - 1] == s3[i - 1]))
            dp[i][0] = r
        for j in range(1, n + 1):
            dp[0][j] = (dp[0][j - 1] and (s2[j - 1] == s3[j - 1]))

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i - 1][j] and (s1[i - 1] == s3[i + j - 1])) or (dp[i][j - 1] and (s2[j - 1] == s3[i + j - 1]))
        return dp[m][n]

s = Solution()
print(s.isInterleave("a", "", "c"))