# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        import copy
        total_res = []
        res = []
        def DFS(r, sum):
            if r is None:
                return

            sum += r.val
            res.append(r.val)
            DFS(r.left, sum)
            DFS(r.right, sum)
            if r.left is None and r.right is None:
                if sum == targetSum:
                    total_res.append(copy.deepcopy(res))
            res.pop(-1)
        DFS(root, 0)
        return total_res

