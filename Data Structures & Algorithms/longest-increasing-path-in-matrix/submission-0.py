''' greater than or equal to 0.
    - non negative

Return the length of the longest strictly increasing path within matrix.
    - so each num increase in the path

From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

from each coord on the grid, we can go 4 dirs dfs and return the max len that we traveled at each dir.
keep track of visited
    - 
Brute: 4^(m*n)
Memo: m*n
 '''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        res = 0
        dir = [(-1,0), (1,0), (0, -1), (0, 1)]
        memo = {}
        def dfs(i , j):
            res = 0

            if (i,j) in memo:
                return memo[(i,j)]

            for dr, dc in dir:
                nr = i + dr
                nc = j + dc
                
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]):
                    if matrix[nr][nc] > matrix[i][j]:
                        res = max(res, dfs(nr, nc))

            memo[(i,j)] = 1 + res
            return 1 + res
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                res = max(res, dfs(i, j))
        return res
                    