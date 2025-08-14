# Last updated: 8/14/2025, 10:00:34 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.left_vals = []
        self.right_vals = []



    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if root is None:
            return True

        if root.left == None and root.right == None:
            return True

        left = root.left
        right = root.right

        if left is not None and right is not None:
            self.dfs_left(left)
            self.dfs_right(right)

            return True if self.left_vals == self.right_vals else False

        else:
            return False

    

    def dfs_left(self, node):

        if node is None:
            self.left_vals.append(None)
            return

        self.left_vals.append(node.val)

        self.dfs_left(node.left)
        self.dfs_left(node.right)



    def dfs_right(self, node):


        if node is None:
            self.right_vals.append(None)  
            return

        self.right_vals.append(node.val)  

        self.dfs_right(node.right)
        self.dfs_right(node.left)
