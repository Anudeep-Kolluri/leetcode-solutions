# Last updated: 8/14/2025, 9:21:29 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == []:
            return root

        queue = [root]

        while queue:

            curr = queue.pop(0)

            if curr:

                queue.append(curr.left)
                queue.append(curr.right)

                curr.left, curr.right = curr.right, curr.left

        
        return root

