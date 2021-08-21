# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent > 0:
            res = 1
            while exponent != 0:
                res = res * base
                exponent -= 1
            return res
        if exponent < 0:
            e = abs(exponent)
            res = 1
            while e != 0:
                res = res * base
                e -= 1
            return 1 / res
s = Solution()
print(s.Power(2.000, 3))
