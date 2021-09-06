"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        hash = {}
        new_head = Node(head.val)
        cur_head = head
        cur_new_head = new_head
        hash[cur_head] = cur_new_head
        while cur_head.next is not None:
            new_node = Node(cur_head.next.val)
            cur_new_head.next = new_node
            cur_head = cur_head.next
            cur_new_head = cur_new_head.next
            hash[cur_head] = cur_new_head

        cur_head = head
        cur_new_head = new_head

        while cur_head is not None:
            if cur_head.random is None:
                cur_new_head.random = None
            else:
                cur_new_head.random = hash[cur_head.random]
            cur_head = cur_head.next
            cur_new_head = cur_new_head.next
        return new_head