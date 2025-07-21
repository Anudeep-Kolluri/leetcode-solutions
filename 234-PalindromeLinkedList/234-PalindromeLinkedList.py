# Last updated: 7/21/2025, 1:00:16 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = copy.deepcopy(head)
        
        rev = None
        start : Optional[ListNode] = head

        while current:
            tmp = rev
            rev, rev.next, current = current, tmp, current.next

        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next

        return True
