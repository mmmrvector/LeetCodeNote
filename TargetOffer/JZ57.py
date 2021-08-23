# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        res = []
        def find_father(p):
            while p.next:
                p = p.next
            return p

        def inorder(root):
            arr = []
            if root.left:
                arr.extend(inorder(root.left))
            arr.append(root)
            if root.right:
                arr.extend(inorder(root.right))
            return arr
        p = find_father(pNode)
        res = inorder(p)
        idx = res.index(pNode)
        if idx + 1 >= len(res):
            return None
        else:
            return res[idx + 1]

