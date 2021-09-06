# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        left = head
        right = self.get_middle(head)
        tmp = right.next
        right.next = None
        right = tmp

        l1 = self.sortList(left)
        l2 = self.sortList(right)
        return self.merge(l1, l2)


    def get_middle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        head = ListNode()
        tail = head
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        while left:
            tail.next = left
            left = left.next
            tail = tail.next
        while right:
            tail.next = right
            right = right.next
            tail = tail.next
        return head.next