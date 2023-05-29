# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pyparsing import Optional


class Solution:
    def reverseList(self, head):
        previous_node = None
        current_node = head
        next_node = None

        while current_node:
            # store the next to next node to avoid the connection break
            next_node = current_node.next

            current_node.next = previous_node  # removed the connection marked to previous connection
            previous_node = current_node  # creating node relation marking

            current_node = next_node  # assigning to holder state

        head = previous_node
        return head
