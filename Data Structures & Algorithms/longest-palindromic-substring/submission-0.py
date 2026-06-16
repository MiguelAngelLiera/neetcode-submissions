class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        j = N
        while j > 0:
            for i in range(0, N-j+1):
                if self.isPalindrome(s[i:i+j]):
                    return s[i:i+j]
            j -= 1
        return ""

    def isPalindrome(self, s: str) -> str:
        N = len(s)
        i = 0
        j = N - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        