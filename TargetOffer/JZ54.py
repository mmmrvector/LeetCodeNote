# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.map = {}
        self.once = ""
        self.s = ""
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        if self.once != '':
            return self.once[0]
        else:
            return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char not in self.map:
            self.map[char] = 1
            self.once += char
        else:
            self.map[char] += 1
            self.once = self.once.replace(char, '')
s  = Solution()
ss =  "google"
out = ""
for i in range(len(ss)):
    s.Insert(ss[i])
    out += s.FirstAppearingOnce()
print(out)