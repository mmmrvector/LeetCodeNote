# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        res = []
        if not pRoot:
            return []
        q = [[pRoot, 0]]
        while len(q) != 0:
            cur = q.pop(0)
            p = cur[0]
            level = cur[1]
            if len(res) <= level:
                res.append([p.val])
            else:
                if level % 2 == 0:
                    res[level].append(p.val)
                else:
                    res[level].insert(0, p.val)
            if p.left:
                q.append([p.left, level + 1])
            if p.right:
                q.append([p.right, level + 1])
        return res
