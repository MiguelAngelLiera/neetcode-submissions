class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        self.d = ''
        for s in strs:
            self.d = self.d + s
        self.d = set(self.d)
        res = {}
        for s in strs:
            a = self.anagram(s)
            t = res.get(a,[])
            res[a] = t + [s]
        return list(res.values())

        
    def anagram(self, s: str) -> bool:
        self.d = dict.fromkeys(self.d,0)
        for i in s:
            self.d[i] = self.d[i] + 1
        res = tuple(self.d.values())
        return res
            