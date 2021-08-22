# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == "":
            return 0

        for i, ss in enumerate(s):
            if ss >= 'a':
                return 0
        res = 0
        str2int = ['0', '1', '2', '3', '4', '5', '6' ,'7', '8', '9']
        l = len(s)
        for i in range(l - 1, -1, -1):
            if s[i] == '+' or s[i] == '-':
                if i != 0:
                    return 0
                else:
                    res = res if s[i] == '+' else -1 * res
            else:
                num = str2int.index(s[i])
                res = res + (num * (10 ** (l - 1 - i)))
        return res
