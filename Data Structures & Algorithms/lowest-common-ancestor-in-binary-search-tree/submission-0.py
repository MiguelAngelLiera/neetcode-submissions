# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        g = p.val if p.val >= q.val else q.val
        l = p.val if p.val < q.val else q.val 
        if not root:
            return None
        if g >= root.val >= l:
            return root
        elif g >= root.val and l >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif g < root.val and l < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        