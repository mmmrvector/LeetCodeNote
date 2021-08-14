class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        res = [['X' for __ in range(n)] for _ in range(m)]
        def flip(x, y):
            if res[x][y] == 'O':
                return
            res[x][y] = 'O'
            if x - 1 >= 0:
                if board[x - 1][y] == 'O':
                    flip(x - 1, y)
            if x + 1 < m:
                if board[x + 1][y] == 'O':
                    flip(x + 1, y)
            if y - 1 >= 0:
                if board[x][y - 1] == 'O':
                    flip(x, y - 1)
            if y + 1 < n:
                if board[x][y + 1] == 'O':
                    flip(x, y + 1)

        for i in range(n):
            if board[0][i] == 'O':
                flip(0, i)
            if board[m - 1][i] == 'O':
                flip(m - 1, i)
        for i in range(m):
            if board[i][0] == 'O':
                flip(i, 0)
            if board[i][n - 1] == 'O':
                flip(i, n - 1)
        for i in range(m):
            for j in range(n):
                board[i][j] = res[i][j]
        return board


s = Solution()
res = s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
print(res)