class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        M = len(word2)
        N = len(word1)
        new = ''
        while i < N or j < M:
            if (i ^ j and j < M) or i == N:
                new += word2[j]
                j += 1
            elif (~(i ^ j) and i < N) or j == len(word2):
                new += word1[i]
                i += 1
        return new
        