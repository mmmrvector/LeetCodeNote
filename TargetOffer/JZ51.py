# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        B = [1 for _ in A]
        for i in range(1, n):
            B[i] = B[i - 1] * A[i - 1]
        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp *= A[i + 1]
            B[i] *=tmp
        return B