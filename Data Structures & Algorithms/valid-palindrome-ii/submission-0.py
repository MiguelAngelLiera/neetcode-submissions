class Solution:
    def validPalindrome(self, s: str) -> bool:
        if self.is_Palindrome(s):
            return True
        for i in range(len(s)):
            if self.is_Palindrome(s[:i] + s[i+1:]):
                return True
        return False


    def is_Palindrome(self, s:str) -> bool:
        n =len(s)
        i = 0
        j = n - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        