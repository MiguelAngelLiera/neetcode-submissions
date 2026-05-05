# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        if root.val == subRoot.val and self.aux_isSubtree(root.left, subRoot.left) and self.aux_isSubtree(root.right, subRoot.right):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False

    def aux_isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        if root.val == subRoot.val and self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right):
            return True
        return False

        