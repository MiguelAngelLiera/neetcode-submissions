# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [root]
        path = []
        visited =[]
        while stack:
            curr = stack.pop()
            path.append(curr)
            visited.append(curr)
            if not curr.right and not curr.left:
                if sum([n.val for n in path]) == targetSum:
                    return True
                else:
                    path.pop()
                    while self.childsVisited(path[-1], visited):
                        path.pop()
                        if not path:
                            break
                    
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return False

    def childsVisited(self, node: TreeNode, visited: List[TreeNode]) -> bool:
        return (not node.left or node.left in visited) and (not node.right or node.right in visited)

            

        