class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        n = len(heights)
        m = len(heights[0])

        for i in range(0, m):
            pacific.add((0, i))
            atlantic.add((n-1, i))
        
        for i in range(0, n):
            pacific.add((i, 0))
            atlantic.add((i, m-1))

        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(i, j, seen):
            seen.add((i,j))
            for dr, dc in dir:
                r = i + dr
                c = j + dc
                if 0 <= r < n and 0 <= c < m:
                    if heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        dfs(r, c, seen)
        for r, c in pacific.copy():
            dfs(r, c, pacific)
        for r, c in atlantic.copy():
            dfs(r, c, atlantic)
            
        res = []
        for r, c in pacific:
            if (r,c) in atlantic:
                res.append([r,c])

        return res