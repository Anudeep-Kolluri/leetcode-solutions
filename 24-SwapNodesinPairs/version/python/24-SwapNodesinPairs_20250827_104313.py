# Last updated: 8/27/2025, 10:43:13 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            # If current node has a duplicate
            if curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Link prev to the node after duplicates
                prev.next = curr.next
            else:
                # No duplicate, move prev
                prev = prev.next
            curr = curr.next

        return dummy.next
