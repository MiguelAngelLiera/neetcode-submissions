class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        r = []
        # [-4,-1,-1,0,1,2]
        for p0, e in enumerate(nums):
            p1 = p0
            p2 = n-1
            while p1 < n and p2 > p0-1 and p1 != p2:
                if (e + nums[p1] + nums[p2]) > 0 or p2==p0:
                    p2 = p2 - 1
                elif (e + nums[p1] + nums[p2]) < 0 or p1==p0:
                    p1 = p1 + 1
                elif (e + nums[p1] + nums[p2]) == 0: 
                    if [e,nums[p1],nums[p2]] not in r:
                        r.append([e,nums[p1],nums[p2]])
                    p1 = p1 +1
        return r
        