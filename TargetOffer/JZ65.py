#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix char字符型二维数组
# @param word string字符串
# @return bool布尔型
#
class Solution:
    def hasPath(self , matrix , word ):
        # write code here
        m = len(matrix)
        n = len(matrix[0])
        isVisited = [[False for _ in range(n)] for __ in range(m)]
        add = []
        def dfs(x, y, w):
            if w == "":
                return True
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            if matrix[x][y] == w[0] and not isVisited[x][y]:
                isVisited[x][y] = True
                r = dfs(x - 1,y, w[1:]) or dfs(x + 1, y, w[1:]) or dfs(x, y -1, w[1:]) or dfs(x, y + 1, w[1:])
                isVisited[x][y] = False
                return r
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
        return False
s = Solution()
print(s.hasPath([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"ABCB"))