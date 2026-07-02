class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        return self.rec_rotate(matrix, 0, N-1)

    def rec_rotate(self, matrix: List[List[int]], zero, n) -> None:
        if n - zero < 0:
            return matrix
        print(zero, n)
        for k in range(0, n-zero):
            b = matrix[zero+k][n] 
            matrix[zero+k][n] = matrix[zero][zero+k] 
            c = matrix[n][n-k] 
            matrix[n][n-k] = b 
            d = matrix[n-k][zero] 
            matrix[n-k][zero] = c 
            matrix[zero][zero+k] = d
        self.rec_rotate(matrix, zero+1, n-1)
        return 
        