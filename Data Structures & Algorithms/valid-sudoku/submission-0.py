class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            if i % 3 == 0:
                d0, d1, d2 = set(), set(), set()
            for j in range(9):
                r = board[i][j]
                c = board[j][i]
                d = j // 3
                if r != '.' and r in row:
                    return False
                if c != '.' and c in col:
                    return False
                if r != '.' and r in eval(f'd{d}'):
                    return False
                
                row.add(r)
                col.add(c)
                eval(f'd{d}').add(r)
        return True
                
            

        