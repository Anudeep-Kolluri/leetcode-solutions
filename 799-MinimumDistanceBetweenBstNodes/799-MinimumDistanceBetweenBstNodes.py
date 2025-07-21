# Last updated: 7/21/2025, 12:59:55 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []

    def dfs(self, root):
        if root == None:
            return None
        
        self.arr.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        return

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        small = 10e7
        for idx, i in enumerate(self.arr[:-1]):
            for j in self.arr[idx+1:]:
                if (y := abs(i-j)) < small:
                    small = y
        
        return small





