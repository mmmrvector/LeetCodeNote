# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        numbers = []
        cur = []
        def generate_number():
            n = len(cur) - 1
            sum = 0
            for i, num in enumerate(cur):
                sum += num * (10 ** (n-i))
            return sum
        def dfs(root):
            if root is None:
                return
            cur.append(root.val)
            if root.left is None and root.right is None:
                num = generate_number()
                numbers.append(num)
                cur.pop(-1)
                return
            if root.left is not None:
                dfs(root.left)
            if root.right is not None:
                dfs(root.right)
            cur.pop(-1)
        dfs(root)
        return sum(numbers)