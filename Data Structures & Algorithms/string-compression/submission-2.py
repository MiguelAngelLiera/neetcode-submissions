class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 1
        N = len(chars)
        c = 1
        while j < N:
            if chars[i] != chars[j]:
                if c > 1:
                    len_ = list(str(c))
                    chars[:] = chars[:i+1] + len_ + chars[j:]
                    j = i+ len(len_)+1
                    print(chars, i, j)
                    N = len(chars)
                i = j
                c = 0 
            j += 1
            c += 1
        
        if c > 1:
            chars[:] = chars[:i+1] + list(str(c))
        return len(chars)

        
        