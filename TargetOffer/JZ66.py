# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        isVisited = [[False for _ in range(cols)] for __ in range(rows)]
        def valid(x, y):
            r = 0
            while x / 10 > 0:
                r = r + x % 10
                x = int(x / 10)
            while y / 10 > 0:
                r = r + y % 10
                y = int(y / 10)
            return r <= threshold
        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return
            if isVisited[x][y]:
                return
            if not valid(x, y):
                return
            self.res += 1
            isVisited[x][y] = True
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
        dfs(0, 0)
        return self.res

s = Solution()
print(s.movingCount(1,2,3))