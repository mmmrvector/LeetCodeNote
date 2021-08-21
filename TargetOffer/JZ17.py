# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 is None or pRoot2 is None:
            return False
        def isSame(p1, p2):
            if p2 is None:
                return True
            if p1 is None:
                return False
            if p1.val == p2.val:
                return isSame(p1.left, p2.left) and isSame(p1.right, p2.right)
            else:
                return False
        q = [pRoot1]
        while len(q) != 0:
            root = q.pop(0)
            if isSame(root, pRoot2):
                return True
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
        return False
