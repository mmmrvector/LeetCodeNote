# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        res = []
        def pre_order(root):
            if root is None:
                return
            res.append(root.val)
            pre_order(root.left)
            pre_order(root.right)

        def build(root):
            if res != []:
                root.left = None
                root.right = TreeNode(res.pop(0))
                build(root.right)

        pre_order(root)
        root.val = res.pop(0)
        build(root)



