# Last updated: 7/21/2025, 1:01:21 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        tmp = output
        carry = 0
        while l1 or l2:
            if l1 and l2:
                #keep adding l1 + l2 values to output
                total = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next

            elif l1 == None:
                #keep adding l2 values to output
                total = l2.val
                l2 = l2.next
                
            elif l2 == None:
                #keep adding l1 values to output
                total = l1.val
                l1 = l1.next

            print(total)

            if carry:
                total += 1
                carry = 0

            if total > 9:
                total = total % 10
                carry = 1
            

            node = ListNode()
            node.val = total
            
            tmp.next = node
            tmp = tmp.next


        if carry:
            node = ListNode()
            node.val = carry
            tmp.next = node
            tmp = tmp.next
            carry = 0

            
        return output.next