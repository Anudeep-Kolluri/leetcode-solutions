# Last updated: 8/14/2025, 8:35:37 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # MUST USE BFS

        if p == q:
            return True

        queue1 = [p]
        queue2 = [q]

        visited1 = []
        visited2 = []

        while queue1 and queue2:

            curr_1 = queue1.pop(0)
            curr_2 = queue2.pop(0)

            first = (curr_1 == None)
            second = (curr_2 == None)

            if first or second:
                if first != second:
                    return False
                else:
                    continue

            elif curr_1.val != curr_2.val:
                return False

            
            if curr_1.left != None or curr_1.right != None:
                queue1.append(curr_1.left)
                queue1.append(curr_1.right)
            
            if curr_2.left != None or curr_2.right != None:
                queue2.append(curr_2.left)
                queue2.append(curr_2.right)

        
        return True if (len(queue1) == 0) and (len(queue2) == 0) else False