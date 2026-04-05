# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p= self.do_bfs(p)
        q = self.do_bfs(q)
        n = len(p)
        m = len(q)
        if n != m:
            return False
        for i in range(n):
            if p[i] != q[i]:
                return False
        return True
    
    def do_bfs(self, t: TreeNode) -> List[int]:
        if t:
            return [t.val] + self.do_bfs(t.left) + self.do_bfs(t.right)
        else:
            return ['null']

        