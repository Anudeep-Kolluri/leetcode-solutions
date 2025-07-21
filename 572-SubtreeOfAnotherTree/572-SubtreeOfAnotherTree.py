# Last updated: 7/21/2025, 1:00:09 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Returns True if 'subRoot' is a subtree of 'root', False otherwise.
        """
        if not root:
            # If root is None, it can only match if subRoot is also None
            return False
        
        # If the trees match starting at this root, return True
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, keep checking subRoot against left and right subtrees of 'root'
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Returns True if the two binary trees 'p' and 'q' are exactly the same
        (same structure and same node values).
        """
        # Both None -> same
        if not p and not q:
            return True
        # One is None, the other isn't -> not the same
        if not p or not q:
            return False
        # Values differ -> not the same
        if p.val != q.val:
            return False
        
        # Recurse on left subtree and right subtree
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
