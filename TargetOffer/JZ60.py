# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res = []
        q = [[pRoot, 0]]
        while len(q) != 0:
            cur = q.pop(0)
            p = cur[0]
            l = cur[1]

            if len(res) <= l:
                res.append([p.val])
            else:
                res[l].append(p.val)
            if p.left:
                q.append([p.left, l + 1])
            if p.right:
                q.append([p.right, l + 1])
        return res