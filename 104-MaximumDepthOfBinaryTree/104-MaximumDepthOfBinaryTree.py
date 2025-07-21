# Last updated: 7/21/2025, 1:01:04 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxLen = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            #Came to end
            return 0
        leftCount = self.maxDepth(root.left)
        rightCount = self.maxDepth(root.right)

        count = max(leftCount, rightCount)

        return count + 1
