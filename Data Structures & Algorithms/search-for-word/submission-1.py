class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(board)
        M = len(board[0])

        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    bckt = self.backtrack(board, i, j, word[1:], set())
                    if bckt:
                        return True

        return False
                    


    def backtrack(self, board: List[List[str]], i, j, word: str, visited) -> bool:
        
        if len(word) == 0:
            return True
        
        visited.add((i, j))
        neigs = self.neighboor(board, i, j)
        for n_i, n_j in neigs:
            if not (n_i, n_j) in visited:
                if board[n_i][n_j] == word[0]:
                    old = visited.copy()
                    bckt = self.backtrack(board, n_i, n_j, word[1:], visited)
                    if bckt:
                        return True
                    visited = old
        return False
        
        
    def neighboor(self, board: List[List[str]], i, j) -> List[int]:
        N = len(board)
        M = len(board[0])

        nei = []
        if i + 1 < N:
            nei.append((i+1, j))
        if j + 1 < M:
            nei.append((i, j+1))
        if i - 1 > -1:
            nei.append((i-1, j))
        if j - 1 > -1:
            nei.append((i, j-1))

        return nei


        