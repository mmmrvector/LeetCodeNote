# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @param k int整型
# @return ListNode类
#
class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        l = 0
        p = pHead
        while p is not None:
            l += 1
            p = p.next
        if k > l:
            return None
        p = pHead
        i = 0
        while i < l - k:
            p = p.next
            i += 1
        return p