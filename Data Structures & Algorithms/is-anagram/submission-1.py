class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _s = set(s)
        _t = set(t)
        if _s != _t:
            return False
        s_seen = dict.fromkeys(_s, 0)
        t_seen = dict.fromkeys(_t, 0)
        for _i in s:
            s_seen[_i] = s_seen[_i] + 1
        for _j in t:
            t_seen[_j] = t_seen[_j] + 1
        print(s_seen)
        print(t_seen)
        return s_seen == t_seen