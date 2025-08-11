# Last updated: 8/11/2025, 10:32:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        self.arr=[]
        self.dfs(root)
        return self.arr


    def dfs(self, node):
        
        if node == None:
            return

        
        self.dfs(node.left)
        self.arr.append(node.val)
        self.dfs(node.right)
            