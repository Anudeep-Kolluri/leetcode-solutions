# Last updated: 8/27/2025, 10:13:28 AM
# chait gpt
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy


        while prev.next and prev.next.next:
            
            _1st_node = prev.next
            _2nd_node = prev.next.next

            prev.next = _2nd_node
            _1st_node.next = _2nd_node.next
            prev.next.next = _1st_node

            prev = prev.next.next

        
        return dummy.next



            