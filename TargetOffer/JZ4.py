# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, vin):
        # write code here

        if len(pre) == 0:
            return None
        if len(vin) == 0:
            return None
        root_val = pre.pop(0)
        idx = vin.index(root_val)
        root = TreeNode(root_val)

        left = self.reConstructBinaryTree(pre, vin[:idx])
        right = self.reConstructBinaryTree(pre, vin[idx+1:])
        root.left = left
        root.right = right
        return root

s=Solution()
s.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])