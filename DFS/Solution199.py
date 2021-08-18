# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def DFS(root, level):
            if not root:
                return
            if len(res) <= level:
                res.append([])
            res[level].append(root.val)
            DFS(root.left, level + 1)
            DFS(root.right, level + 1)
        ret = []
        DFS(root, 0)
        for l in res:
            ret.append(l[-1])
        return ret
