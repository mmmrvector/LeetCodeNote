# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

'''
根节点不光要比左子树大，还要比左子树所有的子树都要大；要比右子树所有的子树要小
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        MIN = -2147483649
        MAX = 2147483648
        def validateBST(root, low, high):
            if root.val <= low or root.val >= high:
                return False
            if root.left and not validateBST(root.left, low, root.val):
                return False
            if root.right and not validateBST(root.right, root.val, high):
                return False
            return True

        if root is None:
            return True
        return validateBST(root, MIN, MAX)


