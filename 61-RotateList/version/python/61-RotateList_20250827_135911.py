# Last updated: 8/27/2025, 1:59:11 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length and last node
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        last = curr
        
        # Step 2: make it circular
        last.next = head
        
        # Step 3: find new head position
        k = k % length
        steps_to_new_head = length - k
        
        # Step 4: move to new tail
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        # Step 5: cut the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head