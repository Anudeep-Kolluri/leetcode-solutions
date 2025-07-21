# Last updated: 7/21/2025, 1:01:00 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        a1 = self.preorderTraversal(root.left)
        a2 = self.preorderTraversal(root.right)

        x = [root.val] + a1 + a2
        
        print(x)

        return x


