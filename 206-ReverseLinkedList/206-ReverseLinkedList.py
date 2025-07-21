# Last updated: 7/21/2025, 1:08:47 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        rev = None
        while current:
            rev, rev.next, current = current, rev, current.next

        return rev