'''
本题希望找到可以同时流向太平洋和大西洋的地点
从题目可知，第一行与第一列的所有点都可以流到太平洋；第m行与第n列的所有点都可以流入大西洋
因此可以从边缘点逆推，即从可以流入太平洋的点逆向流（从低往高），直至最高点，至此找到所有可以流向太平洋的点；
同理找到所有可以流向大西洋的点
可以同时流向太平洋与大西洋的点可以找到
'''
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)
        n = len(heights[0])
        toPacific = [[False for x in range(n)] for y in range(m)]
        toAtlantic = [[False for x in range(n)] for y in range(m)]

        def isValid(x, y, path):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if path[x][y]:
                return False
            return True

        def dfs(x, y, path):
            path[x][y] = True
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            for i in range(4):
                if isValid(x + dx[i], y + dy[i], path) and heights[x][y] <= heights[x + dx[i]][y + dy[i]]:
                    dfs(x + dx[i], y + dy[i], path)

        for i in range(m):
            dfs(i, 0, toPacific)
            dfs(i, n -1, toAtlantic)
        for j in range(n):
            dfs(0, j, toPacific)
            dfs(m - 1, j, toAtlantic)

        res = []
        for i in range(m):
            for j in range(n):
                if toAtlantic[i][j] and toPacific[i][j]:
                    res.append([i, j])
        return res
s = Solution()
s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])



