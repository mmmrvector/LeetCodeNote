# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        l = len(s)
        if l == 0:
            return s
        n = n % l
        s = s[n:] + s[:n]
        return s