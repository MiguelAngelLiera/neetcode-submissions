# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.aux_goodNodes(root, None)
        
    def aux_goodNodes(self, node: TreeNode, max_val: int) -> int:
        if not node:
            return 0
        c = 0
        if not max_val or node.val >= max_val:
            max_val = node.val
            c = 1
        return c + self.aux_goodNodes(node.left, max_val) + self.aux_goodNodes(node.right, max_val)