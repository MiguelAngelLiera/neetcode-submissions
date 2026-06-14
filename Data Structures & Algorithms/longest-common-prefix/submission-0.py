class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sub = strs[0]
        for s in strs:
            while sub not in s:
                sub = sub[:-1]


        return sub
        