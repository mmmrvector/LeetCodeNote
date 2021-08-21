# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        res = []
        p = pHead
        if p is None:
            return None
        while p is not None:
            res.append(p.val)
            p = p.next
        root = ListNode(res.pop(-1))
        p = root
        while len(res) != 0:
            p.next = ListNode(res.pop(-1))
            p = p.next
        return root