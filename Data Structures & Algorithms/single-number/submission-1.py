class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vocab = set([])
        for n in nums:
            if n not in vocab:
                vocab.add(n)
            else:
                vocab.remove(n)

        return next(iter(vocab))
            
            
