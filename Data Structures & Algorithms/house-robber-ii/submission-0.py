class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        mem = [[0, nums[1]],[nums[0], max(nums[0], nums[1])]]

        for i in range(2, N):
            mem[0].append(max(nums[i] + mem[0][i-2], mem[0][i-1]))
            mem[1].append(max(nums[i] + mem[1][i-2], mem[1][i-1]))

            #print(mem)

        w_out_fst = mem[0][-1]
        w_fst = mem[1][-2]

        return max(w_out_fst, w_fst)
