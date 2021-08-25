
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.res = []
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k == 0:
            return None
        # write code here
        def inorder(root):
             if root is None:
                 return
             inorder(root.left)
             #self.res.append(root.val)
             self.res.append(root)
             inorder(root.right)
        inorder(pRoot)
        if k > len(self.res):
            return None
        return self.res[k - 1]

