# Last updated: 8/14/2025, 9:11:51 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p == q:
            return True

        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:

            curr1 = stack1.pop(0)
            curr2 = stack2.pop(0)

            n1 = (curr1 == None)
            n2 = (curr2 == None)

            if n1 or n2:
                if n1 != n2:
                    return False
                else:
                    continue

            elif curr1.val != curr2.val:
                return False

            
            if curr1.left != None or curr1.right != None:
                stack1.insert(0, curr1.right)
                stack1.insert(0, curr1.left)

            if curr2.left != None or curr2.right != None:
                stack2.insert(0, curr2.right)
                stack2.insert(0, curr2.left)

        return True if (len(stack1) == 0) and (len(stack2) == 0) else False
            
