# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        def normalClone(pHead):
            if pHead is None:
                return
            root = RandomListNode(pHead.label)
            root.next = normalClone(pHead.next)
            return root
        def randomClone(root, cur, pHead):
            if cur is None:
                return
            if pHead.random:
                rv = pHead.random.label
                rn = root
                while rn.label != rv:
                    rn = rn.next
                cur.random = rn
            else:
                cur.random = None
            randomClone(root, cur.next, pHead.next)
        root = normalClone(pHead)
        randomClone(root, root, pHead)
        return root