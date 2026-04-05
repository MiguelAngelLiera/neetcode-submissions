# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        q = [root]
        level = 0
        c = 0
        in_level = []
        n = 2**level

        while self.aux(q):
            
            node = q.pop(0)

            if not node:
                q.append(node)
                q.append(node)
            else:
                in_level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            c += 1
            
            
            if c == n or not self.aux(q):
                level += 1
                if in_level:
                    res.append(in_level)
                in_level = []
                c = 0
                n = 2**level

        return res

    def aux(self, queue: List[int]) -> bool:
        for i in queue:
            if i:
                return True
        return False