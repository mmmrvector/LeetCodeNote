# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def build(pre, ino):
            if len(pre) == 0:
                return None
            root = TreeNode(pre[0])
            ind = ino.index(root.val)
            root.left = build(pre[1:ind + 1], ino[:ind])
            root.right = build(pre[ind + 1:], ino[ind + 1:])
            return root
        r = build(preorder, inorder)
        return r
s = Solution()
s.buildTree([3,9,20,15,7], [9,3,15,20,7])

