class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # go right or go down
        dir = [(1,0), (0, 1)]
        memo = {}
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1

            res = 0
            if (i,j) in memo:
                return memo[(i,j)]

            for dr, dc in dir:
                nr = i + dr
                nc = j + dc
                if 0 <= nr < m and 0 <= nc < n:
                    res += dfs(nr, nc)
            
            memo[(i,j)] = res
            return res
        
        return dfs(0,0)