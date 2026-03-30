class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        p_i = 0
        p_f = n-1

        max = 0
        while p_i != p_f:
            h = min(heights[p_i], heights[p_f]) 
            b = p_f-p_i
            a = b*h
            if a > max:
                max = a
        
            if heights[p_i] < heights[p_f]:
                p_i += 1
            else:
                p_f -= 1

        return max
        