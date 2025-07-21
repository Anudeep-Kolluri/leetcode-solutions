# Last updated: 7/21/2025, 12:59:52 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        size = 0

        while current:
            size += 1
            current = current.next

        if size % 2 == 0:
            size = size//2 + 1
        else:
            size = size//2 + 1

        count = 1
        while head:
            if count == size:
                return head
            head = head.next
            count += 1

