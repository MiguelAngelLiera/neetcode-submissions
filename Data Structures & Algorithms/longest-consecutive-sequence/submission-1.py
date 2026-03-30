class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqs = {}
        nums.sort()
        # [2,20,4,10,3,4,5]
        for i in nums:
            if (i - 1) in seqs.keys():
                seqs[i] = seqs[i-1] + 1
            elif i not in seqs.keys():
                seqs[i] = 1
        vals = seqs.values()
        return max(vals) if len(vals) > 0 else 0
                