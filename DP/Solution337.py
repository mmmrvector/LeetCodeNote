# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}

        def max_val(root, level, rob_level):
            if not root:
                return 0
            # 本层不是目标抢劫层
            if rob_level > level:
                return max_val(root.left, level + 1, rob_level) + max_val(root.right, level + 1, rob_level)
            if root in memo:
                return memo[root]
            # 抢劫本层，或不抢劫本层
            rob_cur = root.val + max_val(root.left, level + 1, level + 2) + max_val(root.right,level + 1, level + 2)
            not_rob_cur = max_val(root.left, level + 1, level + 1)+ max_val(root.right, level + 1, level + 1)
            val = max(rob_cur, not_rob_cur)
            memo[root] = val
            return val
        return max(max_val(root, 0, 0), max_val(root, 0, 1))


# NEXT CODE FOR DEBUG
#
# def generate_tree(l):
#     root = TreeNode(l[0])
#     l.pop(0)
#
#     q = [root]
#     while len(l) != 0:
#         r = q.pop(0)
#         lv = l.pop(0)
#         rv = l.pop(0)
#         if lv:
#             left = TreeNode(lv)
#             r.left = left
#             q.append(left)
#         if rv:
#             right = TreeNode(rv)
#             r.right = right
#             q.append(right)
#     return root
#
# root = generate_tree([3,2,3,None,3,None,1])
#
# s = Solution()
# print(s.rob(root))