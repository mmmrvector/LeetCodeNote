# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 中序遍历
        def DFS(node):
            if node:
                DFS(node.left)
                res.append(node)
                DFS(node.right)
        res, s = [], []
        DFS(root)
        for i in range(len(res) - 1):
            if res[i].val >= res[i + 1].val:
                s.append(i)
        if len(s) == 1:
            res[s[0]].val, res[s[0] + 1].val = res[s[0] + 1].val, res[s[0]].val
        else:
            res[s[0]].val, res[s[1] + 1].val = res[s[1] + 1].val, res[s[0]].val