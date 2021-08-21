# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        m, n = len(matrix), len(matrix[0])
        isVisited = [[False for _ in range(n)] for __ in range(m)]
        i, j = 0, 0
        res = []
        while True:
            flag = True
            for x in range(4):
                if x == 0:
                    while j < n and not isVisited[i][j]:
                        flag = False
                        isVisited[i][j] = True
                        res.append(matrix[i][j])
                        j += 1
                    j -= 1
                    i += 1
                elif x == 1:
                    while i < m and not isVisited[i][j]:
                        flag = False
                        isVisited[i][j] = True
                        res.append(matrix[i][j])
                        i += 1
                    i -= 1
                    j -= 1
                elif x == 2:
                    while j >= 0 and not isVisited[i][j]:
                        flag = False
                        isVisited[i][j] = True
                        res.append(matrix[i][j])
                        j -= 1
                    j += 1
                    i -= 1
                else:
                    while i >= 0 and not isVisited[i][j]:
                        flag = False
                        isVisited[i][j] = True
                        res.append(matrix[i][j])
                        i -= 1
                    i += 1
                    j += 1

            if flag:
                return res
s = Solution()
print(s.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))