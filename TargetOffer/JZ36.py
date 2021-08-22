# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        a1 = []
        p1 = pHead1
        p2 = pHead2
        while p1 is not None:
            a1.append(p1.val)
            p1 = p1.next
        while p2 is not None:
            if p2.val in a1:
                return p2
            p2 = p2.next
        return None
