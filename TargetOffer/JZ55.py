# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        isVisited = {}
        p = pHead
        while p is not None:
            if p not in isVisited:
                isVisited[p] = p.val
            else:
                return p
            p = p.next
        return p