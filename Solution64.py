class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        minPath=[[0] * (n + 2)] * (m + 2)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1:
                    minPath[i][j] = minPath[i][j - 1] + grid[i - 1][j - 1]
                elif i != 1 and j == 1:
                    minPath[i][j] = minPath[i - 1][j] + grid[i - 1][j - 1]
                else:
                    minPath[i][j] = min(minPath[i - 1][j] + grid[i - 1][j - 1], minPath[i][j - 1] + grid[i - 1][j - 1])

        return minPath[m][n]

s = Solution()
print(s.minPathSum([[1,2,3],[4,5,6]]))