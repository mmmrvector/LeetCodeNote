# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        def divide(n, m):
            import math
            if m == 1:
                return n
            x = math.ceil(n / m)
            res = x * divide(n - x, m - 1)
            return res
        res = 0
        for i in range(2, number + 1):
            if res < divide(number, i):
                res = divide(number, i)
        return res
s = Solution()
print(s.cutRope(16))
