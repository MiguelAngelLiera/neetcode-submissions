# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_to_p = self.search_path(root, p)
        path_to_q = self.search_path(root, q)
        print([n.val for n in path_to_p])
        last = None
        for i, n in enumerate(path_to_p):
            if len(path_to_q) == i or n != path_to_q[i]:
                break
            last = n
        return last


    def search_path(self, root, p):
        if not root:
            return []
        if root.val == p.val:
            return [root]
        for child in [root.left, root.right]:
            prob_path = self.search_path(child, p)
            if prob_path:
                return [root] + prob_path
        return []
        