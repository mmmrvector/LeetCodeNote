# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.s = ""
    def Serialize(self, root):
        # write code here
        q = [root]
        while len(q) != 0:
            p = q.pop(0)
            if p:
                self.s += str(p.val) + ','
                q.append(p.left)
                q.append(p.right)
            else:
                self.s += '#,'
        self.s = self.s[:-1]
        return self.s

    def Deserialize(self, s):
        # write code here
        arr = s.split(',')
        head = None
        if arr[0] != '#':
            head = TreeNode(int(arr.pop(0)))
        else:
            return head
        q = [head]
        while len(arr) != 0:
            p = q.pop(0)
            lv = arr.pop(0)
            rv = arr.pop(0)
            if lv != '#':
                p.left = TreeNode(int(lv))
                q.append(p.left)
            if rv != '#':
                p.right = TreeNode(int(rv))
                q.append(p.right)
        return head