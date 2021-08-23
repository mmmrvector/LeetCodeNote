#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param pattern string字符串
# @return bool布尔型
#
class Solution:
    def match(self , str , pattern ):
        # write code here
        m = len(str)
        n = len(pattern)

        # dp[i][j] 表示str前i-1位与pattern前j-1位是否匹配。i = 0 或j = 0表示空字符串
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        # 当str为空字符串时，需要考虑*，当pattern为空字符串时，除dp[0][0]外全部为False
        for i in range(1, n + 1):
            y = i - 1
            if pattern[y] == "*":
                dp[0][i] = dp[0][i - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = i - 1
                y = j - 1
                if pattern[y] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[y] == '*':
                    if str[x] == pattern[y - 1] or pattern[y - 1] == '.':
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    if str[x] == pattern[y]:
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
s = Solution()
print(s.match("aaa","aa*"))
