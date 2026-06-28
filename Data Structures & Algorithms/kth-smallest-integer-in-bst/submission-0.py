# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        _inorder = self.inorder(root)
        for n in _inorder:
            k -= 1
            if k == 0:
                break
        
        #print([v.val for v in _inorder])
        return n.val


    def inorder(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []
        return self.inorder(root.left) + [root] + self.inorder(root.right)
        