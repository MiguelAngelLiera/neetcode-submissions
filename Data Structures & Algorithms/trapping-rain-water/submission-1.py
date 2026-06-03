class Solution:
    def trap(self, height: List[int]) -> int:
        r_pointers =[]
        l_pointers = []
        for i in range(len(height)):
            h = height[i]
            if not l_pointers or h >= l_pointers[-1]:
                l_pointers.append(h)
            else:
                l_pointers.append(l_pointers[-1])
            
            h = height[-(i+1)]
            if not r_pointers or h >= r_pointers[0]:
                r_pointers = [h] + r_pointers
            else:
                r_pointers = [r_pointers[0]] + r_pointers

        water = 0
        for i in range(len(height)):
            water += min(l_pointers[i], r_pointers[i]) - height[i]

        return water
