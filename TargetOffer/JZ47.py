# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        # 非常奇怪
        ans = n
        # python 短路？ x = a and b   if a is true, then return b, else return a
        temp = ans and self.Sum_Solution(n - 1)
        ans = ans + temp
        return ans