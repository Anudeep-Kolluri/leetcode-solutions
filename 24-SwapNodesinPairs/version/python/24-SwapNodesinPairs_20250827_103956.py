# Last updated: 8/27/2025, 10:39:56 AM
# kewl
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        prev = ListNode(-999)
        prev.next = curr

        # prev, curr, next

        while curr and curr.next:

            curr_val = curr.val
            next_val = curr.next.val

            if curr_val == next_val:
                
                temp = curr.next.next
                while temp:
                    
                    if temp.val != curr_val:
                        break
                    else:
                        temp = temp.next
                
                curr = prev
                curr.next = temp

                if prev.val == -999:
                    head = curr.next
            
            else:
                prev = curr
                curr = curr.next

        return head


        