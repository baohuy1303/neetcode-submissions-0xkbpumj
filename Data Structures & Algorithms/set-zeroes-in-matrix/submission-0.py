class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        m = len(matrix)
        n = len(matrix[0])
        # use top row for columns, use left col for rows
        top_row_zero = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        top_row_zero = True
                        continue
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, m):
            for j in range(1, n):
        
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for r in range(0, m):
                matrix[r][0] = 0
        if top_row_zero:
            for c in range(0, n):
                matrix[0][c] = 0

        return