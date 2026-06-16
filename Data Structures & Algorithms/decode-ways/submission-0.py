class Solution:
    codex = {
        '1': 'A', '2': 'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', '10':'J',
        '11':'K', '12':'L', '13':'M', '14':'N', '15':'O', '16':'P', '17':'Q', '18':'R', '19':'S',
        '20':'T', '21':'U', '22':'V', '23':'W', '24':'X', '25':'Y', '26':'Z'}
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N < 1:
            return 1
        fst = 1 if self.codex.get(s[0], None) else 0
        mem = [1, fst]

        for k in range(1, N):
            mem.append(0)
            last = 1 if self.codex.get(s[k], None) else 0
            two_last = 1 if self.codex.get(s[k-1:k+1], None) else 0
            #print(f'{last}, {mem[-2]}')
            if last and mem[-2]:
                mem[-1] += mem[-2]
            #print(f'{two_last}, {mem[-3]}')
            if two_last and mem[-3]:
                mem[-1] += mem[-3]

        return mem[-1]

    