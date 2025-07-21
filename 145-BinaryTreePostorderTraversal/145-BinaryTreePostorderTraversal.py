# Last updated: 7/21/2025, 1:00:59 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        a1 = self.postorderTraversal(root.left)
        a2 = self.postorderTraversal(root.right)

        x = a1 + a2 + [root.val]
        
        print(x)

        return x
        