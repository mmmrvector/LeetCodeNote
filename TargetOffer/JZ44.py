# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = s.split(" ")
        s.reverse()
        s = " ".join(s)
        return s