class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vocab = dict.fromkeys(nums,0)
        for n in nums:
            vocab[n] += 1
        
        for k, v in vocab.items():
            if v == 1:
                return k
            
            
