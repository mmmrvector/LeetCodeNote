# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        import copy
        # write code here
        def mirror(root):
            if not root:
                return
            tmp = root.left
            tmp2 = root.right
            root.left = tmp2
            root.right = tmp
            mirror(root.left)
            mirror(root.right)
        def is_same(root1, root2):
            if not root1:
                return not root2
            if not root2:
                return False
            if root1.val == root2.val:
                return is_same(root1.left, root2.left) and is_same(root1.right, root2.right)
            return False
        pRoot2 = copy.deepcopy(pRoot)
        mirror(pRoot2)
        return is_same(pRoot, pRoot2)