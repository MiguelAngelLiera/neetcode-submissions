class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        f = 1
        longest = 0
        n = len(s)
        while i < n and f < n + 1:
            window = s[i:f]
            s_window = set(window)
            if len(window) > len(s_window):
                i += 1
            else:
                if len(window) > longest:
                    longest = len(window)
                f += 1
        return longest
            
        