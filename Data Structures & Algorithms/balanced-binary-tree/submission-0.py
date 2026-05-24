# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h, balanced = self.aux_isBalanced(root)
        return balanced
    
    def aux_isBalanced(self, root: Optional[TreeNode]) -> Tuple(int, bool):
        if root is None:
            return 0, True
        h_left, b_left = self.aux_isBalanced(root.left)
        h_right, b_right = self.aux_isBalanced(root.right)
        balanced = abs(h_left - h_right) <= 1 and b_right and b_left
        return 1 + max(h_left, h_right), balanced 
