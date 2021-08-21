# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def Convert(self , pRootOfTree ):
        if pRootOfTree is None:
            return None
        # write code here
        left = pRootOfTree.left
        right = pRootOfTree.right
        root = pRootOfTree
        if left:
            tree = self.Convert(left)
            root = tree
            t = tree
            while t.right is not None:
                t = t.right
            t.right = pRootOfTree
            pRootOfTree.left = t
        if right:
            tree = self.Convert(right)
            pRootOfTree.right = tree
            tree.left = pRootOfTree

        return root
