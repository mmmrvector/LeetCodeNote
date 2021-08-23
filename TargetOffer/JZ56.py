# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        myHead = ListNode(0)
        myHead.next = pHead
        f = myHead
        p = pHead
        while p is not None:
            flag = False
            while p.next and p.val == p.next.val:
                flag = True
                p = p.next
            if flag:
                f.next = p.next
            else:
                f = p
            p = p.next
        return myHead.next


