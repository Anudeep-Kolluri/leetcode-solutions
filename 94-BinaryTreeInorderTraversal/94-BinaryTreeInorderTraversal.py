# Last updated: 7/21/2025, 1:01:06 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        a1 = self.inorderTraversal(root.left)
        a2 = self.inorderTraversal(root.right)

        x = a1 + [root.val] + a2
        
        print(x)

        return x