# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_, max_, valid = self.aux_isValidBST(root)
        return valid
        


    def aux_isValidBST(self, root: Optional[TreeNode]) -> tuple:
        if not root:
            return float('inf'), -float('inf'), True
        left_min, left_max, left_valid = self.aux_isValidBST(root.left)
        right_min, right_max, right_valid = self.aux_isValidBST(root.right)
        valid = left_max < root.val < right_min and left_valid and right_valid

        return min(left_min, root.val), max(right_max, root.val), valid
        



        # if not root:
        #     return True
        # valid_node = True
        # if root.right:
        #     valid_node = root.right.val > root.val
        # if root.left:
        #     valid_node = valid_node and root.val > root.left.val
        # return valid_node and self.isValidBST(root.left) and self.isValidBST(root.right)
        