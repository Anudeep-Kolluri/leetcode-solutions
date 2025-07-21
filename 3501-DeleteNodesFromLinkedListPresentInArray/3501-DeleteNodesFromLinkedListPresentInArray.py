# Last updated: 7/21/2025, 12:57:57 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        node = head
        prev = None
        while node:
            if node.val in nums:
                if prev:
                    prev.next = node.next
                else:
                    head = node.next
                
                node = node.next
            else:
                prev = node
                node = node.next

        return head

            