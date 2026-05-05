# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     bfs = []
    #     visited = [root]
    #     c = 1
    #     while visited:
    #         elem = visited.pop(0)
    #         c -= 1
            
    #         if elem is not None:
    #             if c == 0:
    #                 q.append(elem)
    #                 c += 2
    #             visited += [elem.left, elem.right]
    #         bfs.append(elem)
        
    #     level = 0

    #     q = []
    #     for i in range(len(bfs)):
    #         n = 2**level
    #         items_in_level = bfs[:n]
    #         bfs = [n:]
    #         while items_in_level:
    #             last = items_in_level.pop()
    #             if last is not None:
    #                 q.append(last)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        rights = [root.val]

        side_view_right = self.rightSideView(root.right)
        side_view_left = self.rightSideView(root.left) 

        levelr = len(side_view_right)
        levell = len(side_view_left)

        if levelr < levell:
            side_view_right += side_view_left[levelr:]
        
        return rights + side_view_right

   

            
        