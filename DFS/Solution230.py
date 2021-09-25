# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.res = None
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(_root):
            if _root is None:
                return
            if _root.left:
                dfs(_root.left)
            self.cnt += 1
            if self.cnt == k:
                self.res = _root.val
            dfs(_root.right)
        dfs(root)
        return self.res
