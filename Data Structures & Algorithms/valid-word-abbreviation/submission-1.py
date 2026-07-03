class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        digits = set([str(n) for n in range (0, 10)])
        i = 0
        j = 0
        while word:
            if not abbr:
                return False
        
            if word[i] == abbr[j]:
                word= word[i+1:]
                abbr = abbr[j+1:]
            elif abbr[j] not in digits or abbr[j] == '0':
                return False
            else:
                while j < len(abbr) and abbr[j] in digits:
                    j += 1
                i = int(abbr[:j])
                if i > len(word):
                    return False
                word = word[i:]
                abbr = abbr[j:]
                j = 0
                i = 0
        
        return True if not abbr else False
            

        