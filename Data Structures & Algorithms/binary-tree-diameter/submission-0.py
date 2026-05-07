# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l, m = self.aux_diameterOfBinaryTree(root)
        return m


    def aux_diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0, 0
        left_h,  max_sum_l = self.aux_diameterOfBinaryTree(root.left)
        right_h, max_sum_r = self.aux_diameterOfBinaryTree(root.right)

        sum_h = left_h + right_h
        return 1 + max(left_h, right_h), max(sum_h, max(max_sum_l, max_sum_r))
        