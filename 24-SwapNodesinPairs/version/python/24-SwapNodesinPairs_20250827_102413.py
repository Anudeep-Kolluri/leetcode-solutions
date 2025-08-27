# Last updated: 8/27/2025, 10:24:13 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr and curr.next:

            curr_val = curr.val
            next_val = curr.next.val

            if curr_val == next_val:
                curr.next = curr.next.next            
            else:
                curr = curr.next

        return head
        