# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_val = []
    def push(self, node):
        # write code here
        self.stack.insert(0, node)
        if len(self.min_val) == 0:
            self.min_val = [node]
        else:
            self.min_val.insert(0, min(self.min_val[0], node))
    def pop(self):
        # write code here
        res = self.stack[0]
        self.stack.pop(0)
        self.min_val.pop(0)
        return res
    def top(self):
        # write code here
        return self.stack[0]
    def min(self):
        # write code here
        return self.min_val[0]
s = Solution()
ops = ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
for op in ops:
    if 'PSH' in op:
        s.push(int(op[3:]))
    elif 'MIN' in op:
        print(s.min())
    elif 'POP' in op:
        s.pop()
    elif 'TOP' in op:
        print(s.top())