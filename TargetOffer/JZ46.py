# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0 or m == 0:
            return -1
        children = [i for i in range(n)]
        s = 0
        while len(children) != 1:
            l = len(children)
            s = s + m - 1
            s = s % l
            children.pop(s)
        return children[0]
s = Solution()
print(s.LastRemaining_Solution(5, 3))