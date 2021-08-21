# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        root = pHead1 if pHead1.val <= pHead2.val else pHead1
        p1 = pHead1
        p2 = pHead2
        if root.val == p1.val:
            p1 = p1.next
        else:
            p2 = p2.next
        r = root
        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                r.next = p1
                p1 = p1.next
                r = r.next
            else:
                r.next = p2
                p2 = p2.next
                r = r.next
        while p1 is not None:
            r.next = p1
            p1 = p1.next
            r = r.next
        while p2 is not None:
            r.next = p2
            p2 = p2.next
            r = r.next
        return root