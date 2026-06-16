class Solution:
    codex = {
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19',
        '20', '21', '22', '23', '24', '25', '26'}
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N < 1:
            return 1
        fst = 1 if s[0] in self.codex else 0
        mem = [1, fst]

        for k in range(1, N):
            mem.append(0)
            last = 1 if s[k] in self.codex else 0
            two_last = 1 if s[k-1:k+1] in self.codex else 0
            if last and mem[-2]:
                mem[-1] += mem[-2]
            if two_last and mem[-3]:
                mem[-1] += mem[-3]

        return mem[-1]

    