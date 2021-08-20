# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        def raw(n):
            res = [0] * 32
            if n < 0:
                res[0] = 1
            n = abs(n)
            for i in range(32):
                if n == 0:
                    break
                if n >= 2 ** (31 -i):
                    res[i] = 1
                    n -= 2 ** (31 - i)
            return res
        def complement(raw):
            for i in range(1, len(raw)):
                raw[i] = 1 - raw[i]
            x = 1
            for i in range(31, 0, -1):
                new_x = int((raw[i] + x) / 2)
                raw[i] = (raw[i] + x) % 2
                x = new_x
            return raw
        code = raw(n)
        if n < 0:
            return sum(complement(code))
        return sum(raw(n))
s = Solution()
print(s.NumberOf1(-1))