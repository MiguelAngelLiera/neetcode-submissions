class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = -1
        canJump = True

        for i in range(2, len(nums)+1):
            jump = nums[-i]
            if jump - i >= final:
                final = -i
                canJump = True
            else:
                canJump = False
        
        return canJump
                