# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.level = 0
    def TreeDepth(self, pRoot):
        # write code here

        def dfs(root, l):
            if root is None:
                return
            self.level = max(self.level, l + 1)
            dfs(root.left, l + 1)
            dfs(root.right, l + 1)
            return
        dfs(pRoot, 0)
        return self.level
