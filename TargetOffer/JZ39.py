# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def is_balance(root, level):
            if root is None:
                return level, True
            level += 1
            left_level, l = is_balance(root.left, level)
            right_level, r = is_balance(root.right, level)
            res = False
            if l and r and abs(left_level - right_level) <= 1:
                res = True
            return max(left_level, right_level), res
        l, r = is_balance(pRoot, 0)
        return r