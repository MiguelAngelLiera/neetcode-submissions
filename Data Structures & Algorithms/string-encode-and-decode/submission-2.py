class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_string = ""
        prefix = ""
        for l in strs:
            enc_string += l
            _l = str(len(l))
            _l = "0"*(3 - len(_l)) + _l
            prefix += _l 
        
        p_tail = 60000 - len(prefix)
        prefix += "-"*p_tail
        
        return prefix + enc_string


    def decode(self, s: str) -> List[str]:
        prefix = s[:60000]
        prefix = self.process_prefix(prefix)
        enc_string = s[60000:]
        strs2 = []
        for p in prefix:
            strs2.append(enc_string[:p])
            enc_string = enc_string[p:]

        return strs2

    def process_prefix(self, prefix: str) -> List[int]:
        final_prefix = []
        while len(prefix) > 0:
            i = prefix[:3]
            if i == "---":
                break
            final_prefix.append(int(i))
            prefix = prefix[3:]

        return final_prefix

