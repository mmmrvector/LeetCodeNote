# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        import copy
        res = []
        def dfs(r, target, pth):
            if r is None:
                return
            if r.val == target and not r.left and not r.right:
                pth.append(r.val)
                res.append(copy.deepcopy(pth))
                pth.pop()
                return
            if r.val > target:
                return
            pth.append(r.val)
            dfs(r.left, target - r.val, pth)
            dfs(r.right, target - r.val, pth)
            pth.pop()
            return
        dfs(root, expectNumber, [])
        return res


