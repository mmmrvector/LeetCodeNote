class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for __ in range(m)]
        area = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or matrix[i][j] == "0":
                    dp[i][j] = int(matrix[i][j]) - 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])+ 1
                if dp[i][j] * dp[i][j] > area:
                    area =  dp[i][j] * dp[i][j]
        return area