# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        q = [root]
        res = []
        while q:
            r = q.pop(0)
            res.append(r.val)
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        return res