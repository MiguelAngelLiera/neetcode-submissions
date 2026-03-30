class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()
        n = len(s)
        s1 = s[:n//2]
        s2 = s[n//2:] if n%2 == 0 else s[n//2 + 1:]
        s2 = s2[::-1]
        return s1 == s2
        