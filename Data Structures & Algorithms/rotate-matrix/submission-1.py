class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # flip vertical
        # transpose (row to col)

        n = len(matrix)        
        m = len(matrix[0])

        for i in range(0, n//2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

        # transpose: iterate from upper main diagonal
        # so no flip twice
        for i in range(0, n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]