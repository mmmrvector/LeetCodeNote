class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for __ in range( m)]
        # cnt = 0
        def travel(x, y):
            if visited[x][y]:
                return 0

            visited[x][y] = True
            if grid[x][y] == "0":
                return 0
            if x - 1 >= 0:
                travel(x - 1, y)
            if x + 1 < m:
                travel(x + 1, y)
            if y - 1 >= 0:
                travel(x, y - 1)
            if y + 1  < n:
                travel(x, y + 1)

            return 1
        cnt = 0
        for x in range(m):
            for y in range(n):
                if travel(x, y):
                    cnt += 1
        return cnt

s= Solution()
s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])